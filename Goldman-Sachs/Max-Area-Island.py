# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

def max(self,grid):
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

        for dr, dc in directions:
            localCounter += dfs(r + dr, c + dc)

        return localCounter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                currentArea = dfs(r,c)
                maxArea = max(maxArea,currentArea)

    return maxArea