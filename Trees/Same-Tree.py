# Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self: 'TreeNode', left: 'TreeNode', right: 'TreeNode', val: int = 0):
        self.val = val
        self.left = left
        self.right = right

    def sameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return ((self.sameTree(p.left,q.left)) and (self.sameTree(p.right,q.right)))