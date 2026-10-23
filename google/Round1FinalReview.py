# Number 1: Number of Islands
# Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
# An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

def numberOfIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r > rows or c > cols:
            return
        if grid[r][c] == 0 or (r,c) in visited:
            return

        visited.add((r,c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r , c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                islands += 1
                dfs(r,c)

    return islands


# Number 2: Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:
# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.
# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.
from collections import deque
def rotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    fresh,time = 0,0
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r,c))


    while fresh > 0 and q:
        for oranges in range(len(q)):
            row, col = q.popleft()

            for dr,dc in directions:
                if grid[row + dr][col + dc] != 1:
                    continue
                if row + dr < 0 or col + dc < 0 or row + dr > rows or col + dc > cols:
                    continue
                grid[row + dr][col + dc] = 2
                fresh -= 1
                q.append((row + dr,col + dc))

        time += 1

    if fresh > 0:
        return -1

    return time

# Number 3: Same Tree
# Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self,val,right,left):
        self.val = val
        self.right = right
        self.left = left

    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False        

        return (self.isSame(p.left,q.left) and self.isSame(p.right,q.right))
