# Number 1: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have to wait after the 
# ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemps(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for x in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[x]:
            index = stack.pop()
            result[x] = x - index
        stack.append(index)

    return result

# Number 2: Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,value):
        
        self.stack.append(value)

        while self.stack:
            if value < self.minStack[-1]:
                value = value
            else:
                value = self.minStack[-1]

        self.minStack.append(value)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

# Number 3: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time.

def longestConsecutiveSeq(nums):
    numSet = set(nums)
    result = 0

    for x in numSet:
        if x - 1 not in numSet:
            length = 1

            while x + length in numSet:
                length += 1

        result = max(result,length)

    return result

# Number 4: Contains Duplicates
# Given an integer array nums return true 
# if any value appears at least twice in the array, and return false otherwise

def containsDuplicates(nums):
    return len(nums) != len(set(nums))

# Number 5: Group Anagrams
# Given an array of strings, group all the anagrams together. THe answer can be returned in any order

def groupAnagrams(strings):
    hashmap = {}

    for x in range(len(strings)):

        key = "".join(sorted(strings[x]))

        if key not in hashmap:
            hashmap[key] = [strings[x]]
        else:
            hashmap[key].append(strings[x])

    return list(hashmap.values())

# Number 5: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and return false otherwise

def isValidAnagram(self,s,t):

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# Number 6: Median of 2 Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def medianOf2SortedArrays(nums1,nums2):

    A,B = nums1,nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A,B = B,A

    l,r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-inf")
        Aright = A[i+1] if (i+1) < len(A) else float("inf")
        Bleft = B[j] if j > 0 else float("-inf")
        Bright = B[j+1] if (j+1) < len(A) else float("inf")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft) / 2)
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

# Number 7: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(target,position,speed):
    pairs = sorted(zip(position,speed),reverse = True)
    stack = []

    for p,s in pairs:
        stack.append(float(target - p)/s)
        while len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# Number 8: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maximumSubarray(nums):
    result = nums[0]
    currentSum = 0

    for x in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += x

        result = max(result,currentSum)

    return result

# Number 9: Best Time to Buy and Sell Stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def bestTime(prices):
    l,r = 0, len(prices)
    result = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[1]
            result = max(result,profit)

        else:
            l = r

        r += 1

    return result

# Number 10: Binary Tree Level Order Trvaersal
# Given the root of a binary tree,
#  return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

from collections import deque
class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def BSTLevelOrder(root):
        q = deque()
        result = []
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for x in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                result.append(level)

        return result


# Number 11: Jump Game
# You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.
# Return `true` *if you can reach the last index, or* `false` *otherwise*.

def jumpGame(nums):
    goal = len(nums) - 1

    for x in range(len(nums) - 2, -1, -1):
        if x + nums[x] >= goal:
            goal = x

    if goal == 0:
        return True

    return False

# Number 12: Max Chunks to Sort
# You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.
# We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return *the largest number of chunks we can make to sort the array*.

def maxChunks(arr):
    largestVal = 0
    maxChunks = 0

    for x in range(len(arr)):
        largestVal = max(largestVal,arr[x])

        if largestVal == x:
            maxChunks += 1

    return maxChunks   


        