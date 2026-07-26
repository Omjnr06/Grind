# Number 1: Longest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def longestRectangleInHistogram(heights):
    maxArea = 0
    stack = [] # index, height

    for x in range(len(heights)):
        start = x
        while stack and stack[x][1] > heights[x]:
            index,height = stack.pop()
            maxArea = max(maxArea, height * (x - index))
            start = index

        stack.append(start,heights[x])

    for i,h in stack:
        maxArea = max(maxArea, h * (len(stack) - i))

    return maxArea

# Number 2: Product of Array except self
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


# Number 3: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(heights):
    result = 0
    l,r = 0, len(heights) - 1

    while l < r:
        area = min(heights[l],heights[r]) * (r-l)
        result = max(result,area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return result


# Number 4: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(position,target,speed):

    pairs = sorted(zip(position,speed),reverse=True)
    stack = []
    

    for p,s in pairs:
        stack.append(float(target - p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# Number 5: Top K Frequent Elements 
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
def topK(nums,k):
    result = []
    hashmap = {}

    for x in range(len(nums)):
        hashmap[x] = 1 + hashmap.get(x,0)

    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap,(hashmap[x],x))

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


# Number 6: Group ANagrams
# Given an array of strings, group all the anagrams together. THe answer can be returned in any order
def groupAnagrams(strings):
    hashmap = {}

    for x in range(len(strings)):
        key = "".join(sorted(strings[x]))
        if key in hashmap:
            hashmap[key].append(strings[x])
        else:
            hashmap[key] = [strings[x]]

    return list(hashmap.keys())

