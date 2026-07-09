# Number 1: Product of array except self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def ProductofArray(nums):
    result = [1] * (len(nums))

    prefix = 1
    for x in range(len(nums)):
        result[x] = prefix
        prefix = prefix * nums[x]


    postfix = 1
    for x in range(len(nums)-1,-1,-1):
        result[x] *= postfix
        postfix = postfix * nums[x]

    return result

# Number 2: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def CarFleet(target,position,speed):
    pairs = sorted(zip(position,speed),reverse=True)
    stack = []

    for p,s in pairs:
        stack.append(float(target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)