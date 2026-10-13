# Number 1: Time Based Key Store 
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

class Timestamp:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key  not in self.store:
            self.store[key] = []
        self.store[key].append([[value,timestamp]])

    def get(self, key: str, timestamp: int) -> int:
        values = self.store.get(key,[])
        l,r = 0, len(values) - 1
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l =  mid + 1

            else:
                r = mid - 1

        return result

# Number 2: Product of Array Except Itself
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productOfArray(nums: list[int]) -> list[int]:
    result = [1] * len(nums)

    prefix = 1
    for x in range(len(nums)):
        result[x] = prefix
        prefix *= nums[x]

    postfix = 1
    for x in range(len(nums) -1, -1, -1):
        result[x] *= postfix
        postfix *= nums[x]


    return result 

# Number 3: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#  and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals: list[list[int]]) -> list[int]:
    intervals.sort(key = lambda i: i[0])
    result = [intervals[0]]

    for start, end in intervals:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(end,lastEnd)
        else:
            result.append([start,end])

    return result


# Number 4: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive 
# elements sequence.* You must write an algorithm that runs in `O(n)` time.

def longestConsecutive(nums: list[int]) -> int:
    numsHash = set(nums)
    maxLength = 0

    for x in numsHash:

        if x - 1 not in numsHash:
            length = 1

            while x + length in numsHash:
                length += 1

        maxLength = max(maxLength,length)


    return maxLength

# Number 5: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait
#  after the ith day to get a warmer temperature. If there is no future day for which 
# this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)

    for x in range(len(temperatures)):
        while stack and temperatures[x] > temperatures[stack[-1]]:
            index = stack.pop()
            result[x] = x - index

        stack.append(temperatures[x])
    return result


# Number 6: Search a 2d Matrix
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.
# You must write a solution in `O(log(m * n))` time complexity.

def search(matrix: list[list[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1

    if not matrix:
        return False

    while top <= bottom:
        midRow = (top + bottom) // 2

        if target > matrix[midRow][cols - 1]:
            top = midRow + 1
        elif target < matrix[midRow][0]:
            bottom = midRow - 1

        else:
            break

    if not(top <= bottom):
        return False

    row = (top + bottom ) // 2
    l,r = 0, len(row) -1

    while l <= r:
        mid = (l + r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1

        else:
            return True


    return False 

# Number 7: Min Stack
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

    def push(self:'minStack', value: int) -> None:
        
        self.stack.append(value)

        if self.minStack:
            value = min(value, self.minStack[-1])
        else:
            value = value

        self.minStack.append(value)

    def pop(self: 'minStack') -> bool:
        self.stack.pop()
        self.minStack.pop()
        return True

    def top(self: 'minStack') -> int:
        return self.stack[-1]

    def getMin(self:'minStack') -> int:
        return self.minStack[-1]
    
# Number 8: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Node:
    def __init__(self: 'Node', val: int = 0, next: 'Node' = None) -> None:
        self.val = val
        self.next = next

    def reverse(head):

        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

# Number 9: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(heights):
    l,r = 0,len(heights) - 1
    result = 0

    while l < r:
        area = min(heights[l],heights[r]) * (r-l)
        result = max(result, area)

        if heights[l] > heights[r]:
            l += 1
        else:
            r -= 1

    return result

# Number 10: Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
import heapq
def topK(nums,k):
    hashmap = {} # frequency list where key = number and value = frequency
    result = []

    for x in nums:
        hashmap[x] = 1 + hashmap.get(x,0)
    

    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap,(hashmap[x],x))

        if len(heap) > k:
            heapq.heappop(heap)


    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result

# Number 11: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

def isValidParentheses(self,s):
    stack = []
    bracketsHash = {"]":"[",")":"(","}":"{"}

    for x in s:
        if x in bracketsHash:
            if stack and stack[-1] == bracketsHash[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append()

    if stack:
        return False

    return True




