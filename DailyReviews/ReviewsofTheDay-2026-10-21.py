# Number 1: Jump Game
# You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.
# Return `true` *if you can reach the last index, or* `false` *otherwise*.

def jumpGame(self,nums):
    goal = len(nums) -1

    for x in range(len(nums) -2, -1 -1):
        if x + nums[x] >= goal:
            goal = x

    if goal == 0:
        return True

    return False

# Number 2: Max Chunks to Sort
# You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.
# We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return *the largest number of chunks we can make to sort the array*.

def maxChunks(arr):
    largestVal = 0
    chunks = 0

    for x in range(len(arr)):
        largestVal = max(largestVal,arr[x])
        if largestVal == x:
            chunks += 1

    return chunks

# Number 3: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def longestRepeating(s,k):
    l = 0
    freqList = {}
    result = 0

    for r in range(len(s)):
        freqList[s[r]] = 1 + freqList.get(s[r],0)

        while max(freqList.values()) - (r-l+1) > k:
            freqList[s[r]] -= 1
            l += 1

        result = max(result,r-l+1)

    return result

# Number 3: Longest Substring without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(s):
    l = 0
    inWindow = set()
    result = 0

    for r in range(len(s)):
        if s[r] in inWindow:
            inWindow.remove(s[l])
            l += 1
        inWindow.add(s[r])
        result = max(result,r-l+1)

    return result

# Number 4: Time Based Key-Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, 
# with `timestamp_prev <= timestamp`. If there are multiple such values, 
# it returns the value associated with the largest `timestamp_prev`.
#  If there are no values, it returns `""`.

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self,key,value,timestamp):

        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value,timestamp])

    def get(self,key,timestamp):

        values = self.store.get(key,[])
        l,r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result

# Number 5: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container. 

def containerWithMostWater(heights):
    l,r = 0,len(heights) -1
    result = 0

    while l < r:
        area = min(heights[l],heights[r]) * (r-l)
        result = max(result,area)

        if heights[l] < heights[r]:
            l += 1

        else:
            r -= 1

    return result

# Number 6: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have to wait 
# after the ith day to get a warmer temperature.
#  If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for x in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[x]:
            index = stack.pop()
            result[x] = x - index
        stack.append(index)

    return result

# Number 7: Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,value):
        self.stack.append(value)
        if self.minStack:
            value = min(self.minStack,value)
        else:
            value = value

        self.minStack.append(value)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


# Number 8: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time.

def longestConsecutive(nums):
    numSet = set(nums)
    count = 0

    for x in numSet:
        if x - 1 not in numSet:
            length = 1
        while x + length in numSet:
            length += 1

        count = max(count,length)

    return count

# Number 8: Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
# There is only **one repeated number** in `nums`, return *this repeated number*.
# You must solve the problem **without** modifying the array `nums` and using only constant extra space. 

def findDuplicate(nums):
    slow,fast = 0,0

    while True:
        slow = nums[slow]
        fast = nums[nums[slow]]

        if fast == slow:
            break

    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow

# Number 9: Balanced BST
# Given a binary tree, determine if it is height-balanced.

class TreeNode:
    def __init__(self,left,right,val):
        self.left = left 
        self.right = right
        self.val = val

    def isBalanced(self,root):
        def dfs(root):
            if not root:
                return [True,0]

            left = self.isBalanced(root.left)
            right = self.isBalanced(root.right)

            balancedVal = (left[0] and right[0] and abs((left[1] - right[1])) <= 1)
            return [balancedVal,1 + max(left[1],right[1])]

        return dfs(root)[0]

# Number 10: Diameter of A BST
# Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.
# The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
# The **length** of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self,right,left,val):
        self.left = left
        self.right = right
        self.val = val
    
    def diameter(self,root):

        self.count = 0

        def dfs(root):
            if not root:
                return 0

            left = self.diameter(root.left)
            right = self.diameter(root.right)
            
            self.count = max(self.count, left + right)

            return 1 + max(left,right)

        dfs(root)
        return self.count

# Number 11: Same Tree
# Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
class TreeNode:
    def __init__(self,right,left,val):
        self.left = left
        self.right = right
        self.val = val

    def sameTree(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return True

        return (self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right))

# Number 12: Median of Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
def medianOfSortedArrays(nums1,nums2):
    A,B = nums1,nums2

    if len(B) < len(A):
        A,B = B,A

    total = len(A) + len(B)
    half = total // 2

    l,r = 0,len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("infinity")
        Aright = A[i+1] if (i + 1) < len(A) else float("-infinity")
        Bleft = B[j] if j > 0 else float("infinity")
        Bright = B[j+1] if (j + 1) < len(B) else float("-infinity") 

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft) / 2)
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

    return

# Number 13: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(target, position, speed):
    stack = []
    pairs = sorted(zip(position,speed), reverse = True)

    for p,s in pairs:
        stack.append(float(target - p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


