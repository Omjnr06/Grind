# Number 1: Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
# There is only **one repeated number** in `nums`, return *this repeated number*.
# You must solve the problem **without** modifying the array `nums` and using only constant extra space.

def duplicateNumber(nums):
    fast = 0
    slow = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[slow]]

        if fast == slow:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]


        if slow == slow2:
            return 

    return -1

# Number 2: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum

def maxSubarray(nums):
    maxVal = 0
    count = 0

    for x in nums:
        if count < 0:
            count = 0

        count += x
        maxVal = max(maxVal, count)

    return maxVal

# Number 3: Best Time to Buy and Sell Stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def bestTime(prices):
    l,r = 0,1 # left is buying price right is selling price
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

        else:
            l = r

        r += 1

    return maxProfit