# Number 1: Trapping Rainwater
# Given n non-negative integers representing an elevation map where the width of each 
# bar is 1, compute how much water it can trap after raining.

def trapping(heights):
    l,r = 0,len(heights) -1
    leftMax = heights[l]
    rightMax = heights[r]
    result = 0

    if not heights:
        return 0
    
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax,heights[l])
            result += leftMax - heights[l]

        else:
            r -= 1
            rightMax = max(rightMax,heights[r])
            result += rightMax - heights[r]

    return result

# Number 2: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def mostWater(heights):
    l,r = 0,len(heights) - 1
    maxAmount = 0

    while l < r:
        area = min(heights[l],heights[r]) * (r-l)
        maxAmount = max(maxAmount,area)

        if heights[l] < heights[r]:
            l += 1

        else:
            r -= 1

    return maxAmount

# Number 3: 3sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def three(nums):
    result = []

    for x in range(len(nums)):

        if x > 0 and nums[x] == nums[x - 1]:
            continue

        l,r = x + 1, len(nums) - 1

        while l <= r:
            threesum = nums[x] + nums[l] + nums[r]

            if threesum > 0:
                r -=1 
            elif threesum < 0:
                l += 1

            else:
                result.append([nums[x],nums[l],nums[r]])
                l += 1
                while l < r and nums[l] == nums[l -1]:
                    l += 1

        return result


# Number 4: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form.
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next

    def reorder(head):
        slow,fast = head, head.next

        while fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        prev = None

        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp

        firstHalf = head
        secondHalf = prev

        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return head

# Number 5: Search in Rotated Sorted Array:
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def search(target,nums):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target > nums[mid] or nums[mid] < nums[l]:
                l = mid + 1

            else:
                r = mid - 1

        else:
            if target < nums[mid] or nums[mid] > nums[r]:
                r = mid - 1
            else:
                l = mid - 1

        return -1 

# Number 6: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1,
#  return the area of the largest rectangle in the histogram.

def largest(heights):
    stack = []
    result = 0

    for x in range(len(heights)):
        start = x

        while stack and stack[x][1] > heights[x]:
            index,height = stack.pop()
            result = max(result, height * (x - index))
            start = index
        stack.append(start,heights[x])

    for i,h in stack:
        result = max(result, h * (len(stack) - i))

    return result

# Number 8: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(position,speed,target):
    pairs = sorted(zip(position,speed),reverse=True)
    stack = []

    for p,s in pairs:
        stack.append(float(target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack [-2]:
            stack.pop()

    return len(stack)

# Number 9: Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productofArray(nums):
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
