# Number 1: Search in A rotated sorted Array
## 
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums,target):
    l,r = 0,len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid -1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1

# Number 2: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time.

def longest(nums):
    numSet = set(nums)
    count = 0

    for x in numSet:
        length = 0
        if x > 0 and x -1 not in numSet:
            length = 1

        while x + length in numSet:
            length += 1

        count = max(count, length)

    return count

# Number 3: Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
def valid(board):
    rows = defaultdict(set())
    cols = defaultdict(set())
    squares = defaultdict(set())

    for r in range(len(board)):
        for c in range(len(board[0])):

            if board[r][c] == ".":
                continue
            
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3][c//3]:
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])

    return True        