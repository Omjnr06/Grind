# Number 1: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def minimumInRotatedSorted(nums):
    result = nums[0]
    l,r = 0,len(nums) - 1

    while l<= r:
        if nums[l] <= nums[r]:
            result = min(result,nums[l])
            break

        mid = (l + r) // 2
        result = min(result, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return result


# Number 2: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(height):
    l,r = 0,len(height) -1
    maxArea = 0

    while l < r:
        currArea = min(height[l],height[r]) * (r- 1)
        maxArea = max(maxArea,currArea)

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return maxArea


# Number 3: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(stack)

    for x in range(len(temperatures)):
        while stack and temperatures[x] > temperatures[stack[-1]]:
            curr = stack.pop()
            result[x] = curr - x
        stack.append(x)

    return result


