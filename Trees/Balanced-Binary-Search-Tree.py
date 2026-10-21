# Given a binary tree, determine if it is **height-balanced**.
class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.right = right
        self.left = left

    def isBalanced(root):
        def dfs(root):
            if not root:
                return [True,0]

            left = dfs(root.left)
            right = dfs(root.right)

            isBalancedBool = ((left[0] and right[0]) and abs(left[1] - right[1]) <= 1)
            return [isBalancedBool,1 + max(left[1],right[1])]

        return dfs(root)[0]

    

