# Number 1: Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values.
#  (i.e., from left to right, level by level).

from collections import deque
class TreeNode:
    def __init__(self,left,right,val):
        self.val = val
        self.right = right
        self.left = left

    def levelOrder(root):

        q = deque()
        result = []
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for x in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                result.append(level)

        return result

