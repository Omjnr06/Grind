# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
# two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants 
# (where we allow **a node to be a descendant of itself**).”
class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.right = right
        self.left = left

    def lowestCommon(self,root,p,q):
        current = root
        
        while current:

            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right 

            else:
                return current