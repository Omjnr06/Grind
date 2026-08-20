# You are given an `m x n` `grid` where each cell can have one of three values:
# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.
# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

from collections import deque

def rotten(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    q = deque()
    fresh,time = 0,0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append([r,c])

    while q and fresh > 0:
        for oranges in range(len(q)):
            row,col = q.popleft()

            for dr,dc in directions:
                if((row + dr) < 0 or (col + dc) < 0 or (row + dr) >= rows or (col + dc) >= cols):
                    continue
                if grid[(row + dr)][(col + dc)] != 1:
                    continue

                grid[(row + dr)][(col + dc)] = 2
                q.append([(row + dr),(col + dc)])
                fresh -= 1

        time += 1

    if fresh > 0:
        return -1

    return time
