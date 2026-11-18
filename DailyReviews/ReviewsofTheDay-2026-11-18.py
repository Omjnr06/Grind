# Number 1: Max Depth of Tree
# Given the `root` of a binary tree, return *its maximum depth*.
# A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self,left,right,val):
        self.right = right
        self.left = left
        self.val= val

    def maxDepth(self,root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


# Number 2: Copy List with Random Pointer
# A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

class Node:
    def init(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.x = x
        self.next = next
        self.random = random

    def copyList(head):
        oldToCopy = {None: None}
        dummy = Node(head)
        current = dummy

        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        current = dummy

        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current=  current.next

        return oldToCopy[head]

# Number 3: Invert Tree
# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self,left,right,val):
        self.val = val
        self.left = left
        self.right = right

    def invert(self,root):
        def dfs(node):
            if not node:
                return 

            node.left,node.right = node.right,node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root

# Number 4: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers.
#  The digits are stored in **reverse order**, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

    def add2Numbers(list1,list2):
        carry = 0
        dummy = Node()
        current = dummy

        while carry or list1 or list2:
            value1 = list1.val if list1 else 0
            value2 = list2.val if list2 else 0

            value = value1 + value2 + carry
            carry = value // 10
            value = value % 10

            current.next = Node(value)

            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return current.next

# Number 5: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key = lambda i : i[0])
    result = [intervals[0]]

    for start,end in intervals:
        lastEnd = result[-1][1]
        if start <= lastEnd:
            result[-1][1] = max(lastEnd,end)
        else:
            result.append([start,end])

    return result

# Number 6: Max Area of Island
# You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) 
# connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the 
# grid are surrounded by water.
# The **area** of an island is the number of cells with a value `1` in the island.
# Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

def maxAreaOfIsland(grid):
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    maxArea = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))

        localCounter = 1

        for dr,dc in directions:
            localCounter += dfs(r + dr,c + dc)

        return localCounter


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                counter = dfs(r,c)
                maxArea = max(maxArea,counter)

    return maxArea 


# Number 7: 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):
        
        if x > 0 and nums[x-1] == nums[x]:
            continue

        l,r = x + 1, len(nums) - 1

        value = nums[x] + nums[l] + nums[r]

        if value > 0:
            r -= 1
        elif value < 0:
            l += 1

        else:
            result.append([nums[x],nums[l],nums[r]])
            l += 1 

            while l < r and nums[l-1] == nums[l]:
                l += 1

    return result

# Number 8: Validate BST
# Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.
# A **valid BST** is defined as follows:
# - The left  of a node contains only nodes with keys **strictly less than** the node's key.
#     subtree
# - The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
# - Both the left and right subtrees must also be binary search trees. 

from collections import deque
class TreeNode:
    def __init__(self,val,right,left):
        self.val = val
        self.left = left
        self.right = right

    def isValid(root):
        q = deque()
        q.append([root,float("-inf"),float("inf")])

        while q:
            node, leftBound, rightBound = q.popleft()

            if node.val < leftBound or node > rightBound:
                return False

            if node.left:
                q.append([node.left,leftBound,node.val])

            if node.right:
                q.append([node.right,node.val,rightBound])

        return True

# Number 9: BST Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

from collections import deque
class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.right = right
        self.left = left

    def BSTRightSide(root):
        q = deque()
        result = []
        q.append(root)

        if not root:
            return []

        while q:
            qLen = len(q)
            rightSide = None

            for x in range(qLen):
                node = q.popleft()

                if node:
                    rightSide = node

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.left)

            if rightSide:
                result.append(rightSide.val)

        return result

# Number 10: Lowest Common Ancestor 
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` 
# that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.left = left
        self.right = right

    def lca(self,root,p,q):
        current = root

        while current:
            if current.val > p.val and current.val > q.val:
                current = current.left

            elif current.val < p.val and current.val < q.val:
                current = current.right

            else:
                return current

# Number 11: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Node:
    def __init__(self,next,val):
        self.val = val
        self.next = next

    def reverse(head):
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev