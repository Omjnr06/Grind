# Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
def maximum(nums):
    maxSub = nums[0]
    currentSum = 0

    for x in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += x
        maxSub = max(maxSub,currentSum)

    return maxSub