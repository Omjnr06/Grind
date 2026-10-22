# Number 1: Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
# two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants 
# (where we allow **a node to be a descendant of itself**).”

class TreeNode:
    def __init__(self,left,right,val):
        self.val = val
        self.right = right
        self.left = left

    def lowestCommon(self,root,p,q):
        current = root

        while current:

            if p.val < root.val and q.val < root.val:
                current = current.left

            elif p.val > root.val and q.val > root.val:
                current = current.right

            else:
                return current

# Number 2: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maximumSubarray(nums):
    currentSum = 0
    maxSub = nums[0]

    for x in nums:
        if currentSum < 0:
            currentSum  = 0
        
        currentSum += x

        maxSub = max(maxSub,currentSum)

    return maxSub

# Number 3: Best Time to buy and sell stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def bestTime(prices):
    l,r = 0,1 # left is buying price, while right is selling price
    result = 0

    for x in range(len(prices)):
        
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            result = max(result,profit)

        else:
            l = r

        r += 1

    return result
        