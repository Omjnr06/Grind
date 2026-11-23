# Number 1: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`.
#  You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def longestRepeating(s,k):
    l = 0
    hashmap = {}
    result = 0

    for r in range(len(r)):

        hashmap[s[r]] = 1 + hashmap.get(s[r],0)

        while abs(max(hashmap.values()) - ( r - l + 1)) > k:
            hashmap[s[l]] -=1 
            l += 1

        result = max(r - l + 1, result)

    return result

# Number 2: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

import math
def kokoEating(piles,h):
    
    l,r = 1, max(piles)
    result = l

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(float(p)/k)

        if hours <= h:
            result = min(result, hours)
            r = k - 1

        else:
            l = k + 1

    return result

# Number 3: Encode and Decode String
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is 
# decoded back to the original list of strings.

def encode(strings):
    result = ""

    for x in strings:
        result += len(x) + "*" + x

    return result

def decode(string):
    result = []
    i = 0

    while i < len(string):
        j = i

        while string[j] != "*":
            j +=1 

        length = int(string[i:j])
        i = j + 1
        j = i + length

        result.append(string[i:j])
        i = j

    return result

# Number 4: Top K Frequent Elements
# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

import heapq
def topK(nums,k):
    hashmap = {}
    heap = []
    result = []

    for x in nums:
        hashmap[x] = 1 + hashmap.get(x,0)

    for x in hashmap.keys():
        heapq.heappush(heap,hashmap[x],x)

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result

# Number 5: Validate BST
# Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.
# A **valid BST** is defined as follows:
# - The left  of a node contains only nodes with keys **strictly less than** the node's key.
#     subtree
# - The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
# - Both the left and right subtrees must also be binary search trees.

from collections import deque
class TreeNode:
    def __init__(self,left,right,val):
        self.left = left
        self.right = right
        self.val = val

    def validateBST(root):

        if not root:
            return True
        
        q = deque()
        q.append([root,float("-inf"),float("inf")])

        while q:

            node, leftBound, rightBound = q.popleft()

            if not(leftBound < node.val < rightBound):
                return False

            if node.left:
                q.append([node.left,leftBound,node.val])

            if node.right:
                q.append([node.right,node.val,rightBound])

        return True

# Number 6: BST Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

from collections import deque
class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.left = left
        self.right = right

    def BSTRightSide(root):
        q = deque()
        q.append(root)
        result = []

        while q:
            rightSide = None
            qLen = len(q)

            for x in range(qLen):
                node = q.popleft()

                if node:
                    rightSide = node

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if rightSide:
                result.append(rightSide.val)

        return result

# Number 7: Longest Substring without Any Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
def longestSubstringNoRepeatingChars(s):
    l = 0
    seen = set()
    result = 0

    for r in range(len(s)):
        if s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])

        result = max(result, r - l + 1)

    return 

# Number 8: Time Based Key Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

class Timestamp:
    def __init__(self):
        self.store = {}

    def set(self,key,value,timestamp):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value,timestamp])

    def get(self,key,timestamp):
        values = self.store.get(key,[])
        l,r = 0,len(values)
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if timestamp <= values[mid][1]:
                result = values[mid][0]
                r = mid + 1

            else:
                l = mid + 1

        return result

# Number 9: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(heights):
    l,r = 0, len(heights) - 1
    result = 0

    while l < r:
        area = min(heights[l],heights[r]) * (r-l) 
        result = max(result,area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return result

            
