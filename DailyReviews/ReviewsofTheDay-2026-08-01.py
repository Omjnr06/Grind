# Number 1: Trapping Rainwater
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trappingRainwater(heights):
    if not heights:
        return 0
    
    l,r = 0,len(heights) - 1
    leftMax = heights[l]
    rightMax = heights[r]
    result = 0

    while l < r:
        if leftMax > rightMax:
            l += 1
            leftMax = max(leftMax,heights[l])
            result += leftMax - heights[l]
        else:
            r -= 1
            rightMax = max(rightMax,heights[r])
            result += rightMax - heights[r]

    return result

# Number 2: Time Based Key Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. 
# If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

class Timestamp:
    def __init__(self):
        self.store = {}

    def set(self,key,value,timestamp):
        if self.key not in self.store:
            self.store[key] = [[value,timestamp]]
        self.store[key].append([[value,timestamp]])

    def get(self,key,timestamp):
        values = self.store.get(key,[])
        l,r = 0,len(values)-1
        result = 0

        while l <= r:
            mid = (l + r) // 2
            

            if timestamp <= values[mid][1]:
                result = min(result, values[mid][0])
                l = mid + 1
            else:
                r = mid - 1

        return result


# Number 3: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def minimum(nums):
    l,r = 0, len(nums) - 1
    result = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result, nums[l])
            break

        mid = (l + r) // 2
        result = min(result,nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1

        else:
            r = mid -1

    return result


# Number 4: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(heights):
    l,r = 0,len(heights) - 1
    maxArea = 0

    while l < r:
        currArea = (min(heights[l],heights[r]) * (r-l))
        maxArea = max(maxArea,currArea)

        if heights[l] > heights[r]:
            r -=1
        else:
            l += 1

    return maxArea

# Number 5: 3sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def ThreeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):
        l = x + 1
        r = len(nums) -1 

        if x > 0 and nums[x] == nums[x - 1]:
            continue

        while l < r:
            threesumValue = nums[x] + nums[l] + nums[r]

            if threesumValue > 0:
                r -= 1
            elif threesumValue < 0:
                l += 1

            else:
                result.append([nums[x],nums[l],nums[r]])
                l += 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return result



# Number 6: Two Sum II Input Array is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSumII(target,nums):
    l,r = 0, len(nums) -1

    while l < r:
        value = nums[l] + nums[r]
        if value > target:
            r -= 1
        elif value < target:
            l += 1
        else:
            return [[l+1,r+1]]

    return
