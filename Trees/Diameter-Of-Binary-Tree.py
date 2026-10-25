# Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.
# The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
# The **length** of a path between two nodes is represented by the number of edges between them.

class TreeNode(object):
    def __init__(self: 'TreeNode' = None, left: 'TreeNode' = None, right: 'TreeNode' = 0, val: int = 0) ->'TreeNode':
        self.left = left
        self.right = right
        self.val = val

    def diameter(self,root):
        self.result = 0

        def dfs(current):

            if not current:
                return 0

            left = dfs(current.left)
            right = dfs(current.right)

            self.result = max(self.result, left + right)

            return 1 + max(left,right)

        dfs(root)
        return self.result