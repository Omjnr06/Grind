# Number 1: Number of Islands
# Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
# An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

def numberofIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == "0" or (r,c) in visited:
            return

        visited.add((r,c))

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c)  not in visited:
                islands += 1
                dfs(r,c)

    return islands

# number 2: course schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def schedule(self,numCourses,prerequisites):
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


