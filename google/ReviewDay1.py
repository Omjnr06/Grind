# Number 1: Two Sum - Input Array is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twosumII(nums,target):
    l,r = 0, len(nums) - 1

    while l < r:
        current = nums[l] + nums[r]
        if current > target:
            r -= 1
        elif current < target:
            l += 1
        else:
            return [l+1, r+1]

    return -1

# Number 2: Two Sum
# Given an array and a target return the indices of the two numbers such that they add up to target
def twoSum(nums,target):
    hashmap = {} #  key: difference  value = index

    for x in range(len(nums)):
        difference = target - nums[x]
        if difference in hashmap:
            return [x,hashmap[difference]]
        else:
            hashmap[nums[x]] = x

    return -1

# Number 3: Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.

class Password:
    def encode(strings):
        result = ""
        for x in strings:
            result += len(x) + "*" + x

        return result

    def decode(string):
        result = []
        i = 0

        while i < len(string):
            j = i
            while string[j] != "*":
                j += 1
            length = int(string[i:j])
            i = j + 1
            j = i + length
            result.append(string[i:j])
            i = j

        return result 

# Number 4: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time

def longestSequence(nums):
    maxLength = 0
    numSet = set(nums)

    for x in numSet:
        if x - 1 not in numSet:
            length = 1
        while x + length in numSet:
            length += 1

        maxLength = max(maxLength,length)

    return maxLength

# Number 5: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(target,position,speed):
    pairs = sorted(zip(position,speed),reverse=True)
    stack = []

    for p,s in pairs:
        stack.append(float((target-p)/(s)))
        if len(stack) >=2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# Number 6: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def longestRectangle(heights):
    stack = [] # index, height
    maxArea = 0

    for x in range(len(heights)):
        start = x
        while stack and stack[x][1] > heights[x]:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (x - index))
            start = index
        stack.append(start, heights[x])

    for i,h in stack:
        maxArea = max(maxArea, h * (len(stack) - i))

    return maxArea


