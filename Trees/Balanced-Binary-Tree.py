# Given a binary tree, determine if it is height-balanced.

class TreeNode:
    def __init__(self: 'TreeNode' = None, left: 'TreeNode' = None, right: 'TreeNode' = None, val: int = 0):
        self.right = right
        self.left = left
        self.val = val

    def isBalanced(root: 'TreeNode'):

        def dfs(root):
            if not root:
                return [True,0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = ((left[0] and right[0]) and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]


        