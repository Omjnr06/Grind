# Number 1: Invert Tree
# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self,left,right,val):
        self.right = right
        self.left = left
        self.val = val


    def invert(self,root):
        
        if not root:
            return 

        root.right,root.left = root.left,root.right

        self.invert(root.left)
        self.invert(root.right)

        return root

# Number 2: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self,val,next):
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

            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next

# Number 3: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key = lambda i: i[0])
    result = [intervals[0]]

    for start, end in intervals:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(lastEnd,end)
        else:
            result.append([start,end])

    return result

# Number 4: Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:
# - `0` representing an empty cell
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.
# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

from collections import deque
def rottingOranges(grid):
    q = deque()
    fresh,time = 0,0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                fresh += 1
            if grid[r][c] == "2":
                q.append([r,c])

    while q and fresh > 0:
        for rottenOranges in range(len(q)):
            row, col = q.popleft()

            for dr, dc in directions:
                if row + dr < 0 or col + dc < 0 or row + dr > rows or col + dc > cols:
                    continue
                if grid[row + dr][col + dc] != "1":
                    continue

                grid[row + dr][col + dc] = 2
                q.append([row+dr,col + dc])
                fresh -= 1

        time += 1

    if fresh > 0:
        return -1 

    return time


# Number 5: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.)
#  You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxAreaOfIsland(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]

    visited = set()

    maxArea = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))

        localCounter = 1

        for dr, dc in directions:
            localCounter += dfs(r + dr,c + dc)

        return localCounter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                counter = dfs(r,c)

                maxArea = max(maxArea,counter)

    return maxArea


# Number 6: Threesum
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def Threesum(nums):
    result = []
    nums.sort()

    for x in range(nums):
        
        if x > 0 and nums[x -1] == nums[x]:
            continue

        l = x + 1
        r = len(nums) - 1

        while l < r:
            value = nums[x] + nums[l] + nums[r]
            if value > 0:
                r-= 1
            elif value < 0:
                l += 1
            else:
                result.append([nums[x],nums[r],nums[l]])
                l += 1
                while l < r and nums[l - 1] == nums[l]:
                    l += 1

        return result 




