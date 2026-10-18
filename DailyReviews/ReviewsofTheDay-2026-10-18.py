# Number 1: Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
# There is only **one repeated number** in `nums`, return *this repeated number*.
# You must solve the problem **without** modifying the array `nums` and using only constant extra space.

def findDuplicate(nums: list[int]) -> int:
    fast = 0 
    slow  = 0

    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]

        if fast == slow:
            break

    slow2 = 0

    while True:
        slow2 = nums[slow2]
        slow = nums[slow]

        if slow == slow2:
            return slow

# Number 2: Max Depth of Tree
# Given the `root` of a binary tree, return *its maximum depth*.
# A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left

    def maxDepth(self,root):

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Number 3: Invert Tree
# Given the root of a binary tree, invert the tree, and return its root.

def invertTree(self,root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root

# Number 4: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers. 
# The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self: 'Node', val: int = 0, next: 'Node' = None) -> 'None':
        self.val = val
        self.next = next

    def add2Numbers(list1,list2):
        carry = 0
        dummy = Node(0)
        current = dummy

        while list1 or list2 or carry:
            value1 = list1.val if list1 else 0
            value2 = list2.val if list2 else 0

            value = value1 + value2 + carry
            carry = value // 10
            value = value % 10

            current.next = Node(value)

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            current = current.next

        return dummy.next

# Number 5: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key = lambda i:i[0])
    result = [intervals[0]]

    for start, end in intervals:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(lastEnd,end)
        else:
            result.append(start,end)

    return result


# Number 6: Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:

# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.

# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.
from collections import deque
def rottingOranges(grid):
    rows = len(grid)
    cols = len(grid[0])
    fresh,time = 0,0
    directions = [[1,0],[-1,0],[0,-1],[0,1]]
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r,c))

    while q and fresh > 0:
        for oranges in range(len(q)):
            row, col = q.popleft()

            for dr,dc in directions:
                if row + dr < 0 or row + dr > rows or col + dc < 0 or col + dc > cols:
                    continue

                if grid[row + dr][col + dc] != 1:
                    continue

                fresh -= 1
                grid[row + dr][col + dc] = 2
                q.append((row + dr,col + dc))


        time += 1

    if fresh > 0:
        return -1

    return time

# Number 7: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxArea(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    result = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))

        localCounter = 1

        for dr, dc in directions:
            localCounter += dfs(r + dr, c + dc)

        return localCounter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                counter = dfs(r,c)
                result = max(result,counter)

    return result

# Number 8: Threesum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x - 1]:
            continue
        l,r = x + 1, len(nums) - 1

        while l < r:
            value = nums[x] + nums[l] + nums[r]

            if value > 0:
                r -= 1
            elif value < 0:
                l += 1
            else:
                result.append([nums[x],nums[l],nums[r]])
                l += 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return result

            