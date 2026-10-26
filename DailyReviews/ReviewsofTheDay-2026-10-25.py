# Numer 1: Validate BST
# Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.
# A **valid BST** is defined as follows:
# - The left  of a node contains only nodes with keys **strictly less than** the node's key.
#     subtree
# - The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
# - Both the left and right subtrees must also be binary search trees.

from collections import deque
class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.right = right
        self.left = left

    def validateBST(root):
        q = deque()
        result = []
        q.append([root,float("-inf"),float("inf")])

        while q:
            node,leftBound, rightBound = q.popleft()

            if not (leftBound < node.val < rightBound):
                return False


            if node.left:
                q.append([node.left,leftBound,node.val])

            if node.right:
                q.append([node.right,node.val,rightBound])

        return True


# Number 2: BST Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
from collections import deque
class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.right = right
        self.left = left

    def rightSide(self,root):
        q = deque()
        result = []

        q.append(root)

        while q:
            qLen = len(q)
            rightNode = None

            for x in range(qLen):
                
                node = q.popleft()

                if node:
                    rightNode = node

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            if rightNode:
                result.append(rightNode.val)

        
        return result

# Number 3: Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` 
# that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”
from collections import deque
class TreeNode:
    def __init__(self,val,left,right):
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

# Number 4: Max Depth of Tree
# Given the `root` of a binary tree, return *its maximum depth*.
# A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.
class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.right = right
        self.left = left

    def maxDepth(self,root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Number 5: Invert Tree
# Given the root of a binary tree, invert the tree, and return its root.
class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.right = right
        self.left = left

    def invert(self,root):

        if not root:
            return None

        root.left,root.right = root.right,root.left

        self.invert(root.left)
        self.invert(root.right)

        return root 

# Number 6: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, 
# and each of their nodes contains a single digit. Add the two numbers and 
# return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self, val: int = 0, next: 'Node' = None) -> 'Node':
        self.next = next
        self.val = val

    def add2Numbers(list1,list2):
        dummy = Node(0)
        carry = 0
        current = dummy

        while list1 or list2 or carry:
            
            value1 = list1.val if list1 else 0
            value2 = list2.val if list2 else 0

            value = value1 + value2 + carry
            carry = value // 10 
            value = value % 10

            current.next = Node(value)

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            current = current.next

        return dummy.next

# Number 7: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi],
#  merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

def mergeIntervals(intervals):
    intervals.sort(key= lambda i:i[0])
    result = [intervals[0]]

    for start,end in intervals:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(end,lastEnd)
        else:
            result.append([start,end])

    return result

# Number 8: Rotting Oranges
# You are given an `m x n` `grid` where each cell can have one of three values:
# - `0` representing an empty cell,
# - `1` representing a fresh orange, or
# - `2` representing a rotten orange.
# Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
# Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1` 
from collections import deque
def rottingOranges(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    fresh,time = 0,0
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1

            if grid[r][c] == 2:
                q.append((r,c))

    while fresh > 0 and q:
        for rottingOranges in range(len(q)):
            row, col = q.popleft()

            for dr, dc in directions:
                if (row + dr) < 0 or (col + dc) < 0 or (row + dr) >= rows or (col + dc) >= cols:
                    continue
                
                if grid[(row + dr)][(col + dc)] != 1:
                    continue

                grid[(row + dr)][(col + dc)] = 2
                q.append((row + dr,col + dc))
                fresh -= 1

        time += 1

    if fresh > 0:
        return -1
    
    return time

# Number 9: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxArea(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    result = 0
    visited = set()

    def dfs(r,c):
        
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        localCounter = 1
        visited.add(r,c)

        for dr,dc in directions:
            localCounter += dfs(r + dr,c + dc)

        return localCounter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                area = dfs(r,c)
                result = max(result,area)

    return result

# Number 10: Threesum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):
        l = x + 1
        r = len(nums) - 1

        if x > 0 and nums[(x - 1)] == nums[x]:
            continue

        while l < r:
            value = nums[x] + nums[l] + nums[r]

            if value > 0:
                r -= 1 
            
            elif value < 0:
                l += 1

            else:
                result.append(nums[x],nums[l],nums[r])
                l += 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return result
