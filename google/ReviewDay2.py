# Number 1: Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# needs work, struggled on it a bit.
# I first sort the array and create a resulting array
# then we create the outer for loop which was our k pointer. 
# a very important clause is that the solution set must not have any duplicates.
# we make sure x > 0 and that the number at x is not the same as the number before it. If it is we just continue
# we set our left pointer to be 1 + the for loop pointer
# we set the right pointer to be the length of the string
# then we do a standard 2 pointer approach we loop while l < r
# we then calculate the threesum values at the curr index (nums[l] + nums[r] + nums[x])
# then if the threesum value is > 0 we increase the left pointer.
#  if the threesum value is < 0 we reduce the right pointer
# else we add the 3 numbers because it means they sum to 0 and we move only the left pointer to 1
# then after we check while the left < right and if the numebr at the left pointer is the same as the numeber previous to it we keeep incrementing left pointer.
def threeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x-1]:
            continue

        l = x + 1
        r = len(nums) - 1

        while l < r:
            threesum = nums[l] + nums[r] + nums[x]
            if threesum > 0:
                l += 1
            elif threesum > 0:
                r -= 1
            else:
                result.append([nums[l],nums[r],nums[x]])
                l += 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1

        return result

# Number 2: Best time to Buy and sell Stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.
def stockCheck(prices):
    # l,r = 0,1  left = buy right = sell
    result = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            result = max(result, profit)
        else:
            l = r
        r += 1

    return result

# Number 3: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# create a currentsum and result variables, loop thru the array, cheeck if the currentsum < 0 if it is reset to 0, then add the current # to the current sum,
#  then check if the current sum is  bigger than the global max if it is set to global max
def maxiumumSubarray(nums):
    currentSum = 0
    result = 0

    for x in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += x
        result = max(result,currentSum)

    return result

# Number 4: Rotting Oranges
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
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    q = deque()
    fresh = 0
    time = 0

    # pass 1: account for all fresh oranges and rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                 fresh += 1
            if grid[r][c] == 2:
                q.append((r,c))

    # PASS 2: keep going until out of fresh or rotten oranges

    while fresh > 0 and q:
        for oranges in range(len(q)):
            row,col = q.popleft()
            for dr,dc in directions:
                if row + dr < 0 or col + dc < 0 or row + dr >= rows or col + dc >= cols:
                    continue
                if grid[row+dr][col+dc] != 1:
                    continue
         
                grid[row + dr][col + dc] = 2
                fresh -= 1
                q.append((row + dr,col + dc))

            time += 1

    if fresh > 0:
        return - 1

    return time

