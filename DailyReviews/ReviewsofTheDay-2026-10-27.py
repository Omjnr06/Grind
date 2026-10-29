# Number 1: Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque
class TreeNode:

    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def BSTLevelOrderTraversal(root):
        q = deque()
        result = []
        q.append(root)

        while q:
            level = []
            qLen = len(q)

            for x in range(qLen):

                node = q.popleft()

                if node:
                    level.append(node.val)

                    if node.right:
                        q.append(node.right)

                    if node.left:
                        q.append(node.left)

            if level:
                result.append(level)

        return result

# Number 2: Balanced BST
# Given a binary tree, determine if it is height-balanced.

class TreeNode:

    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def isBalanced(root):
        def dfs(node):
            
            if not node:
                return [True,0]

            left = dfs(node.left)
            right = dfs(node.right)

            isBalanced = ((left[0] and right[0]) and abs(left[1] - right[1]) <= 1)

            return [isBalanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]

# Number 3: Diameter of a Binary Search Tree
# Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.
# The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
# The **length** of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def diameter(self,root):

        self.result = 0

        def dfs(node):
            
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, left + right)

            return 1 + max(left,right)

        dfs(root)
        return self.result

# Number 4: Same Tree
# Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def isSame(self,p,q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSame(q.right,p.right) and self.isSame(p.left,q.left))

# Number 5: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def longestRepeating(s,k):
    l = 0
    hashmap = {}
    result = 0

    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

        while ((r-l+1) - max(hashmap.values()) > k):
            hashmap [s[l]] -= 1
            l += 1

        result = max(result, r - l + 1) 

    return result

# Number 6: Longest Substring without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(s):
    characterSet = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in characterSet:
            set.remove(s[l])
            l += 1

        characterSet.add(s[r])
        result = max(result, r - l + 1)

    return result

# Number 7: Time Base Key Store Value
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously,
#  with `timestamp_prev <= timestamp`. If there are multiple such values, 
# it returns the value associated with the largest `timestamp_prev`. 
# If there are no values, it returns `""`.

class Timestamp:
    def __init__(self: 'Timestamp') -> None:
        self.store = {}

    def set(self: 'Timestamp', key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value,timestamp])

    def get(self:'Timestamp', key: str, timestamp: int) -> int:
        values = self.store[key]
        l,r = 0, len(values) - 1
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if timestamp <= values[mid][1]:
                result = values[mid][0]
                r = mid - 1

            else:
                l = mid + 1

        return result

# Number 8: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def container(heights):
    l = 0 
    r = len(heights) - 1
    result = 0

    while l < r:
        area = min(heights[l],heights[r]) * (r -l)
        result = max(result, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return result

# Number 9: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith 
# day to get a warmer temperature. If there is no future day for which this is possible, 
# keep answer[i] == 0 instead.
def DailyTemperatures(temperatures):

    result = [0] * len(temperatures)
    stack = []

    for x in range(len(temperatures)):
        while stack and temperatures[x] > temperatures[stack[-1]]:
            currIndex = stack.pop()
            result[x] = x - currIndex
        stack.append(currIndex)

    return result