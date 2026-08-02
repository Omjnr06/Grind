# Number 1: Reverse a Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list

def reverseLinkedList(head):
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# Number 2: Longest Rectangle in Histogram: 
# Given an array of integers `heights` representing 
# the  histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

def longest(heights):
    stack = [] # index, height
    result = 0

    for x in range(len(heights)):
        start = x
        while stack and stack[x][1] > heights[x]:
            index, height = stack.pop()
            result = max(result, height * (x - index))
            start = index
        stack.append(start,heights[x])

    for i,h in stack:
        result = max(result, h * (len(stack) - i))

    return result

# Number 3: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(position,speed,target):
    pairs = sorted(zip(position,speed),reverse= True)
    stack = []

    for p,s in pairs:
        stack.append(float(p-target)/s)
        if len(stack) >= 2 and stack[-1] <= stack [-2]:
            stack.pop()

    return len(stack)


# Number 4: Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productofArray(nums):

    result = [1] * (len(nums))

    prefix = 1
    for x in range(len(nums)):
        result[x] = prefix
        prefix *= nums[x]

    postfix = 1
    for x in range(len(nums)-1,-1,-1):
        result[x] *= postfix
        postfix *= nums[x]

    return result

# Number 5: Median of 2 SORTED Arrays:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def median(nums1,nums2):
    A,B = nums1,nums2
    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A,B = B,A

    l,r = 0,len(A) -1 

    while True:
        i = (l + r) // 2
        k = half - i - 2

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) <= len(A) else float("infinity")
        Bleft = B[k] if k >= 0 else float("-infinity")
        Bright = B[k + 1] if (k + 1) <= len(A) else float("infinity")

        if Aleft < Bright and Bleft < Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2

        elif Aleft > Bright:
            r = k - 1
        else:
            l = k + 1

    return 
        