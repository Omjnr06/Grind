# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).
from collections import deque

class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.right = right
        self.left = left


    def BSTLevelOrder(root):
        q = deque()
        result = []
        q.append(root)

        while q:

            qLength = len(q)
            level = []

            for x in range(qLength):
                node = q.popleft()
            
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                result.append(level)

        return result


