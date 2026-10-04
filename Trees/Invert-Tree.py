# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invert(self,root):
        
        if not root:
            return None

        root.left,root.right = root.right,root.left

        self.invert(root.left)
        self.invert(root.right)

        return root