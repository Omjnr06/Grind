# Number 1: Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
# There is only **one repeated number** in `nums`, return *this repeated number*.
# You must solve the problem **without** modifying the array `nums` and using only constant extra space.

def findTheDuplicate(nums):
    fast , slow = 0, 0

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

# Number 2: Validate BST
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

        q = deque()
        q.append([root,float("-infinity"),float("infinity")])

        if not root:
            return True

        while q:            
            node,leftBound,rightBound = q.popleft()
            
            if node.val < leftBound or node.val > rightBound:    
                return False

            if node.left:
                q.append(node.left,leftBound,node.val)

            if node.right:
                q.append(node.right,node.val,rightBound)

        return True

# Number 3: BST Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
from collections import deque
class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def rightSideView(root):

        if not root:
            return []
        
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

# Number 4: Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def lca(self,root,p,q):
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right 

            else:
                return current

# Number 5: Jump Game
# You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.
# Return `true` *if you can reach the last index, or* `false` *otherwise*.

def jumpGame(nums):
    goal = len(nums) - 1

    for x in range(len(nums)-2,-1,-1):
        if x + nums[x] >= goal:
            goal = x

    if goal == 0:
        return True
    
    return False

# Number 6: Max Chunks to Sort
# You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.
# We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return *the largest number of chunks we can make to sort the array*.

def maxChunks(arr):
    largest = 0
    chunks = 0

    for x in range(len(arr)):
        largest = max(largest,arr[x])

        if largest == x:
            chunks += 1

    return chunks


