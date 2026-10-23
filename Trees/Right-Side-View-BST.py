# Given the root of a binary tree, 
# imagine yourself standing on the right side of it,
#  return the values of the nodes you can see ordered from top to bottom.

from collections import deque
class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.right = right
        self.left = left

    def rightSide(root):

        if not root:
            return []
        
        q = deque()
        result = []

        q.append(root)
        while q:
            rightSide = None
            qLength = len(q)

            for x in range(qLength):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                result.append(rightSide.val)

        return result


        