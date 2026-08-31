# Number 1: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums,target):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r ) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[l]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


# Number 2: Valid Palindrome
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

def valid(s):
    l,r = 0, len(s) - 1

    def isAlpha(c):
        return (ord("a") <= ord(c) <= ord("z") or 
                ord("A") <= ord(c) <= ord("Z") or 
                ord("0") <= ord(c) <= ord("9"))

    while l < r:

        while l < r and not isAlpha(s[l]):
            l += 1
        while l < r and  isAlpha(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
    
        l += 1
        r -= 1

    return True

# Number 3: Longest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1,
#  return the area of the largest rectangle in the histogram.

def longest(heights):
    stack = [] # index,height
    maxArea = 0

    for x in range(len(heights)):
        start = x
        while stack and stack[x][1] > heights[x]:
            index, height = stack.pop()
            maxArea = max(maxArea, (height * (x - index)))
            start = index
        stack.append([start,heights[x]])

    for i,h in range((len(stack))):
        maxArea = max(maxArea, h * (len(stack) - i))

    return maxArea

# Number 4: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination

def carFleet(position,speed,target):
    pairs = sorted(zip(position,speed),reverse=True)
    stack = []

    for p,s in pairs:
        stack.append(float(target - p)/s)

        while len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)
