# Number 1: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

import math
def kokoEatingBananas(piles,h):
    l,r = 1, len(max(piles))
    result = l

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for x in piles:
            hours += math.ceil(float(x)/h) 

        if hours <= h:
            result = min(result, hours)
            r = k - 1
        else:
             l = k + 1

    return result

# Number 2: Top K frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order

import heapq
def topK(nums,k):

    hashmap = {}
    result = []

    for x in range(len(nums)):
        hashmap[nums[x]] = 1 + hashmap.get(nums[x],0)


    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap,hashmap[x],x)

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result

# Number 3: Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
# There is only **one repeated number** in `nums`, return *this repeated number*.
# You must solve the problem **without** modifying the array `nums` and using only constant extra space.

def findDuplicate(nums):
    fast,slow = 0,0

    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]

        if fast == slow:
            break


    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow
            break

    return

# Number 4: Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque   
class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def levelOrder(root):
        q = deque()
        result = []

        q.append(root)

        while q:
            level = []
            qLen = len(q)

            for x in range(qLen):
                node = q.popleft()
                
                if node:
                    level.append(node)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            if level:
                result.append(level)

        return result

# Number 5: Balanced BST
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

            isBalanced = (left[1] and right[1] and abs(left[0] - right[0]) <= 1)

            return [isBalanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]

# Number 6: Diameter of Binary Tree
# Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.
# The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
# The **length** of a path between two nodes is represented by the number of edges between them.
class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def diameter(self, root):
        self.result = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result,left + right)

            return 1 + max(left,right)

        dfs(root)

        return self.result

# Number 7: Same Tree
# Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def isSameTree(self,p,q):
        
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right))


# Number 8: Jump Game
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

# Number 9: Max Chunks to Sort
# You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.
# We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return *the largest number of chunks we can make to sort the array*.

def maxChunks(arr):
    chunks = 0
    largestVal = 0

    for x in range(len(arr)):
        largestVal = max(largestVal,arr[x])
        if largestVal == x:
            chunks += 1

    return chunks

# Number 10: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def longestRepeatingCharacter(s,k):
    l = 0
    hashmap = {}
    result = 0

    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

        while (abs(max(hashmap.values())- (r-l +1))) > k:
            hashmap[s[l]] -= 1
            l += 1

        result = max(result,r-l+1)

    return result

# Number 11: Longest Substring without any repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(s):
    l = 0
    seen = set()
    result = 0

    for r in range(len(s)):
        
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])

        result = max(result,r-l+1)

    return result
