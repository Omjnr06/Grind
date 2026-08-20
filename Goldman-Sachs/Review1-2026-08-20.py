# Number 1: Number of Islands
# Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
# An **island** is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.

def numberOf(grid):
    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    visited = set()

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c > cols:
            return

        if grid[r][c] == "0" or (r,c) in visited:
            return

        visited.add((r,c))
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row,col) not in visited:
                islands += 1
                dfs(row,col)

    return islands

# Number 2: Course Schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def schedule(numCourses,prerequisites):
    adjList = {i: [] for i in range(numCourses)}

    for c,p in prerequisites:
        adjList[c] = p

    visiting = set()

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

# Number 3: Max area of island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxAreaof(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    maxArea = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))
        localCounter = 1

        for dr,dc in directions:
            localCounter += dfs(r + dr, c + dc)

        return localCounter

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row,col) not in visited:
                currentArea = dfs(row,col)
                maxArea = max(maxArea,currentArea)

    return maxArea

