# Number 1: Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:
# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange
# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

from collections import deque
def rotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    fresh,time = 0,0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1

            if grid[r][c] == 2:
                q.append([r,c])

    while fresh > 0 and q:
        for rotten in range(len(q)):
            row, col = q.popleft()

            for dr,dc in directions:
                if ((row + dr) < 0 or (col + dc) < 0 or (row + dr) >= rows or (col + dc) >= cols):
                    continue
                if grid[row + dr][col + dc] != 1:
                    continue

                grid[row + dr][col + dc] = 2
                fresh -= 1
                q.append([row + dr,col + dc])

        time += 1

    if fresh > 0:
        return -1

    return time 

# Number 2: Max Area Island
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
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))
        localCounter = 0

        for dr,dc in directions:
            localCounter += dfs(r + dr,c + dc)

        return localCounter

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row,col) not in visited:
                currentArea = dfs(row,col)
                maxArea = max(maxArea,currentArea)

    return maxArea

#  Number 3: Course Schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSched(prerequisites,numCourses):
    adjList = {i:[] for i in range(numCourses)}
    visiting = set()

    def dfs(course):
        if course in visiting:
            return False
        if adjList[course] == []:
            return True

        visiting.add(course)

        for prereq in adjList[course]:
            if not dfs(course):
                return False

        visiting.remove(course)
        adjList[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True

# Number 4: Number of Islands
# Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
# An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

def numberOfIslands(grid):
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

        dfs(r + 1,c)
        dfs(r - 1,c)
        dfs(r,c + 1)
        dfs(r,c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                islands += 1
                dfs(r,c)

    return islands

# Number 5: Remove Nthh Node from End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
    def remove(head,n):
        dummy = Node(0,head)
        slow = dummy
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next



