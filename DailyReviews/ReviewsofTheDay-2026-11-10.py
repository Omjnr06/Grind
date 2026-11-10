# Number 1: Max Depth of Tree
# Given the `root` of a binary tree, return *its maximum depth*.
# A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def maxDepth(self,root):
        if not root:
            return 0

        left = root.left
        right = root.right

        return 1 + max(self.maxDepth(left),self.maxDepth(right))

# Number 2: Trapping Rainwater
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

def trappingRainwater(heights):
    l,r = 0,len(heights) - 1
    leftMax,rightMax = heights[l], heights[r]
    result = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, heights[l])
            result += leftMax - heights[l]

        else:
            r -= 1
            rightMax = max(rightMax, heights[r])
            result += rightMax - heights[r]

    return result

# Number 3: Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, 
# which could point to any node in the list, or null.

class Node:
    def init(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def copyList(head):
        oldToCopy = {None:None}
        current = head

        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        current = head

        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next


        return oldToCopy[head]


# Number 4: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def minimumInRotSorted(nums):
    l,r = 0,len(nums) - 1
    result = nums[l]

    while l <= r:
        
        if nums[l] < nums[r]:
            result = min(result,nums[l])
            break

        mid = (l + r) // 2
        result = min(result, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return result


# Number 5: Valid Palindrome
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.
def validPalindrome(self,s):
    l,r = 0, len(s) - 1

    while l < r:

        while l < r and not self.isAlphaNum(s[l]):
            l += 1 

        while r > l and not self.isAlphaNum(s[r]):
            r -= 1

        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True

def isAlphaNum(self,c):
    return ((ord("a") <= ord(c) <= ord("z")) or (ord("A") <= ord(c) <= ord("Z")) or (ord("0") <=  ord(c) <= ord("9")))

# Number 6: Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
def isValidSudoku(board):

    rows = defaultdict(set())
    cols = defaultdict(set())
    squares = defaultdict(set())

    for r in range(len(board)):
        for c in range(len(board[0])):

            if board[r][c] == ".":
                continue
            
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])


    return True