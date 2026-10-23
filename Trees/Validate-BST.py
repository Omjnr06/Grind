# Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.
# A **valid BST** is defined as follows:
# - The left  of a node contains only nodes with keys **strictly less than** the node's key.
#     subtree
# - The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
# - Both the left and right subtrees must also be binary search trees.

from collections import deque

class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.right = right
        self.left = left

    def isValid(root):

        q = deque()

        if not root:
            return True
        
        q.append([root, float("-inf"), float("inf")])

        while q:
            node, leftBound, rightBound = q.popleft()

            if not(leftBound < node.val < rightBound):
                return False

            if node.left:
                q.append(node.left,)
        
