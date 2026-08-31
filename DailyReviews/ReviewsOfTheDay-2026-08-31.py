# Number 1:Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:

# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.

# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

from collections import deque
def rotting(grid):
    fresh, time = 0,0
    q = deque()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r,c])

    while q and fresh > 0:
        for orange in range(len(q)):
            row,col = q.popleft()

            for dr,dc in directions:
                if ((r + dr) < 0 or (c + dc) < 0 or (r + dr) >= rows or (c + dc) >= cols):
                    continue

                if grid[(r + dr)][(c + dc)] != 1:
                    continue

                grid[(r + dr)][(c + dc)] = 2
                fresh -= 1
                q.append([(r + dr),(c + dc)])

        time += 1

    if fresh > 0:
        return -1
    return time

# Number 2: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.
def maxArea(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    maxArea = 0

    def dfs(r,c):
        if (r < 0 or c < 0 or r >= rows or c >= cols):
            return 0
        if grid[r][c] == 0 or (r,c) in visited:
            return 0
        
        visited.add((r,c))
        localCounter = 1

        for dr,dc in directions:
            localCounter += dfs((r + dr),(c + dc))

        return localCounter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                currentArea = dfs(r,c)
                maxArea = max(maxArea,currentArea)

    return maxArea

# Number 3: Course Schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSched(numCourses, prerequisites):
    adjList = {i: [] for i in range(numCourses)}
    visiting = set()

    for course, prereq in prerequisites:
        adjList[course] = prereq

    def dfs(course):
        if course in visiting:
            return False

        if adjList[course] == []:
            return True

        visiting.add(course)

        for prereq in adjList[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)
        adjList[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


# Number 4: Two Sum II - Input Array is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSumII(nums, target):
    l,r = 0,len(nums) - 1

    while l < r:
        value = nums[l] + nums[r]
        if value > target:
            r -= 1
        elif value < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return 