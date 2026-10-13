# Number 1: Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
# There is only **one repeated number** in `nums`, return *this repeated number*.
# You must solve the problem **without** modifying the array `nums` and using only constant extra space.

def findTheDuplicate(nums):
    slow,fast = 0,0

    while True:
        slow = nums[slow]
        # same as fast.next.next in standard linked list definitions
        fast = nums[nums[fast]]

        if fast == slow:
            break

    slow2 = 0 

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

# either or is the duplicate in this case.
        if slow == slow2:
            return slow

# Number 2: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

class Node:
    def __init__(self, val: int, next: 'Node') -> 'Node':
        self.val = val
        self.next = next


    def isCycle(head: 'Node') -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Number 3: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def searchInSortedRotated(nums: list[int], target: int) -> int:
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[l]:
                r = mid -1 
            else:
                l = mid + 1

    return -1

# Number 4: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def largestRectangle(heights: list[int]) -> int:
    stack = []
    result  = 0

    for x in range(len(heights)):
        start = x

        while stack and stack[x][1] > heights[x]:
            index, height = stack.pop()
            result = max(result, height * (x - index))
            start = index

        stack.append(start,heights[x])

    for i,h in stack:
        result = max(result, h * (len(stack) - i))

    return result

# Number 5: Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:
# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.
# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.


from collections import deque
def rottingOranges(grid: list[list[int]]) -> int:

    q = deque()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    fresh,minutes = 0, 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append((r,c))

    while fresh > 0 and q:
        for rottenOrange in range(len(q)):
            row,col = q.popleft()
            
            for dr,dc in directions:
                if row + dr > rows or col + dc > cols or row + dr < 0 or cols + dc < 0:
                    continue

                if grid[row + dr][col + dc] != 1:
                    continue

                fresh -= 1
                q.append((row+dr , col+dc))
                grid[row + dr][col + dc] = 2

        time += 1

    if fresh > 0:
        return -1

    return time 

# Number 6: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxAreaOfIsland(self,grid):
    
    rows = len(grid)
    cols = len(grid[0])
    maxArea = 0
    seen = set()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]

    def dfs(r,c):
        if ((r >= rows) or (c >= cols) or (r < 0) or (c < 0)):
            return 0

        if grid[r][c] == 0 or (r,c) in seen:
            return 0 

        seen.add((r,c))

        localCounter = 1

        for dr, dc in directions:
            localCounter += dfs((r + dr,c + dc))

        return localCounter


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in seen:
                area = dfs(r,c)
                maxArea = max(maxArea, area)


    return maxArea

# Number 7: Course Schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSchedule (numCourses, prerequisites):
    adjList = {i: [] for i in range(len(numCourses))}
    visiting = set()

    for c,p in prerequisites:
        adjList[c].append(p)

    def dfs(course):

        if course in visiting:
            return False
        
        if adjList[course] ==  []:
            return True

        visiting.add(course)

        for prereq in adjList[course]:
            if not dfs(prereq):
                return False

        adjList[course] = []
        visiting.remove(course)
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True

# Number 8: Threesum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threesum(nums: list[int]) -> list[list[int]]:
    result = []

    if not nums:
        return 0

    for x in range(len(nums)):
        l = x + 1
        r = len(nums) - 1

        if x > 0 and nums[x] == nums[x-1]:
            continue
        while l <=r :
            threesumVal = nums[l] + nums[r] + nums[x]

            if threesumVal > 0:
                r -= 1
            elif threesumVal < 0:
                l += 1
            else:
                result.append([nums[x],nums[l],nums[r]])
                l += 1
                
                while l <= r and nums[l] == nums[l -1]:
                    l += 1

    return result

# Number 9: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:

    def __init__(self, val: int, next: 'Node')-> 'Node':
        self.val = val
        self.next = next

    def reorder(head):
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        secondHalf = slow.next
        prev = None

        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp

        firstHalf = head
        secondHalf = prev

        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2
 
