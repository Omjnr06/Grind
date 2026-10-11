# Number 1: Trapping Rainwater
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trapping(heights: list[int]) -> int:
    l,r = 0, len(heights) - 1
    leftMax = heights[l]
    rightMax = heights[r]
    result = 0

    if not heights:
       return 0
    
    while l < r:
        if heights[l] > heights[r]:
            l += 1
            leftMax = max(leftMax, heights[l])
            result += leftMax - heights[l]

        else:
           r -= 1
           rightMax = max(rightMax, heights[r])
           result += rightMax - heights[r]

    return result

# Number 2: Valid Palindrome
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

def isValidPalindrome(self, s: str) -> bool:
    l,r = 0, len(s) - 1

    while l < r:
        while l < r and not self.isAlphaNumeric(s[l]):
            l += 1

        while r > l and  not self.isAlphaNumeric(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        
        else:
            l += 1
            r -= 1

    return True

def isAlphaNumeric(self,c):
    return (ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"))


# Number 3: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*. 
def longestRepeatingChars(s: str, k: int) -> int:
    result = 0
    l = 0
    freqList = {} # key = character, value = frequency of it in window

    for r in range(len(s)):
        freqList[s[r]] = 1 + freqList.get(s[l], 0)

        while ((r - l + 1) - max(freqList.values())) > k:
            freqList[s[l]] -= 1
            l += 1

        result = max(result, r-l+1)


    return result

# Number 4: Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.
# For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.
# Return *the head of the copied linked list*.
# The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
# - `val`: an integer representing `Node.val`
# - `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.
# Your code will **only** be given the `head` of the original linked list.

class Node:
    def init(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def copy(head: 'Node') -> 'Node':
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

# Number 5: Longest Substring without any repeating characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(s: str) -> int:
    l = 0
    count = 0
    seen = set()

    for r in range(1,len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])

        count = max(count, r-l+1)

    return count


# Number 6: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.


def minimum(nums: list[int]) -> int:
    l,r = 0, len(nums) - 1
    result = result[l]

    while l <= r:
        
        if nums[l] < nums[r]:
            result = min(result,nums[l])
            break

        mid = (l + r) // 2
        result = min(result,nums[mid])

        if nums[l] > nums[mid]:
            r = mid - 1

        else:
            l = mid + 1

    return result


# Number 7: Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
def isValidSudoku(board: list[list[str]]) -> bool:

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