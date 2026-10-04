# Number 1: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    seen = set()
    maxArea = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] != 1 or (r,c) in seen:
            return 0

        seen.add((r,c))

        localArea = 1
        for dr,dc in directions:
            localArea += dfs(dr,dc)

        return localArea

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in seen:
                loopArea = dfs(r,c)
                maxArea = max(maxArea,loopArea)

    return maxArea

# Number 2: Product of Array Except Itself
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productOfArray(nums):
    result = [1] * len(nums)

    prefix = 1
    for x in range(len(nums)):
        result[x] = prefix
        prefix *= nums[x]

    postfix = 1
    for x in range(len(nums)-1,-1,-1):
        result[x] *= postfix
        postfix *= nums[x]


    return result


# Number 3: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

import math
def kokoEating(piles,h):
    l,r = 1, max(piles)
    result = l

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        if hours <= h:
            result = min(result,k)
            r = k - 1

        else:
            l = k + 1

    return result

