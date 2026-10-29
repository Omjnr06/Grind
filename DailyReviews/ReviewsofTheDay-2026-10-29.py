# Number 1: Min Stack
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
        self.minStack = []
        self.stack = []

    def push(self,value: int) -> None:
        self.stack.append(value)

        if self.minStack:
            value = min(value,self.minStack[-1])
        else:
            value = value

        self.minStack.append(value)

    def pop(self):
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


# Number 2: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time.

def longestConsecutive(nums):
    numSet = set(nums)
    result = 0

    for x in numSet:
        length = 0
        if (x - 1) not in numSet:
            length = 1

        while (x + length) in numSet:
            length += 1

        result = max(result,length)

    return result

# Number 3: Validate BST
# Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.
# A **valid BST** is defined as follows:
# - The left  of a node contains only nodes with keys **strictly less than** the node's key.
#     subtree
# - The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
# - Both the left and right subtrees must also be binary search trees.

from collections import deque
class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def validateBST(root):
        q = deque()
        q.append([root,float("-inf"),float("inf")])

        while q:
            qLen = len(q)
            node,leftBound,rightBound = q.popleft()

            if node <= leftBound and node >= rightBound:
                return False

            if node.left:
                q.append([node.left,leftBound,node.val])

            if node.right:
                q.append([node.right,node.val,rightBound])

        return True

# Number 4: BST Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
from collections import deque

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def BSTRightSideView(root):
        q = deque()
        result = []
        q.append(root)

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


# Number 5: Lowest Common Ancestor 
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants 
# (where we allow **a node to be a descendant of itself**).”
from collections import deque

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def lowestCommonAncestor(self,root,p,q):
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = root.left

            elif p.val > current.val and q.val > current.val:
                current = root.right

            else:
                return current.val


        return 

# Number 6: Median of 2 Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def medianOfSorted(nums1,nums2):
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
        Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
        Bleft = B[j] if j > 0 else float("-inf")
        Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

        if Aleft <= Bright and Bleft <= Bright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return min(Aright,Bright) + max(Aleft,Bleft) / 2

        elif Aleft > Bright:
            r = i - 1

        else:
            l = i + 1

    return

# Number 7: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(target,position,speed):
    pairs = sorted(zip(position,speed), reverse = True)
    stack = []

    for p,s in pairs:
        stack.append(float(target-p)/s)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# Number 8: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maximumSub(nums):
    result = 0
    currentSum = 0

    for x in nums:
        if currentSum < 0:
            currentSum = 0

        currentSum += x
        result = max(currentSum,result)

    return result

# Number 9: Best Time to Buy and Sell Stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def bestTime(prices):
    result = 0
    l = 0
    r = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]

        else:
            l = r

        r += 1

        result = max(result,profit)

    return result
