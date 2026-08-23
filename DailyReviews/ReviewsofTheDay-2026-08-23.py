# Number 1: Search in Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums,target):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            elif target < nums[mid] or target > nums[r]:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[l]:
                r = mid -1
            elif target > nums[mid] or target > nums[r]:
                l = mid + 1

    return -1

# Number 2: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the 
# width of each bar is 1, return the area of the largest rectangle in the histogram.

def largest(heights):
    stack = [] # index, height
    result = 0

    for x in range(len(heights)):
        start = x
        while stack and stack[-1][1] > heights[x]:
            index,height = stack.pop()
            result = max(result, height * (x - index))
            start = index
        stack.append(start,heights[x])

    for i,h in range(len(stack)):
        result = max(result, h * (len(stack)- i))

    return result

# Number 3: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(position,speed,target):
    pairs = sorted(zip(position,speed),reverse= True) # [[p1,s1],[p2,s2]]
    stack = []

    for p, s in pairs:
        stack.append(float(target - p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)       


# Number 4: Best Time to Buy and Sell Stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def bestTime(prices):
    l,r = 0,1 # l = buy, r = sell
    result = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            result = max(result, profit)
        else:
            l = r

        r += 1

    return result

#  Number 5: Merge Intervals:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key= lambda i: i[0]) # mini function to sort your interval and then were sorting by the start value
    result = []

    for start, end in intervals:
        if result[-1][1] >= start:
            result[-1][1] = max(result[-1][1],end)
        else:
            result.append([start,end])

    return result

