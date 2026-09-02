# Number 1: Best Time to buy and sell stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def buyandSell(prices):
    l,r = 0,1 # left = buying right = selling
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit,profit)
        else:
            l = r

        r += 1

    return maxProfit

# Number 2: Merge Intervals 
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
def intervalsMerge(intervals):
    intervals.sort(key= lambda i: i[0])
    result = [intervals[0]]

    for start,end in intervals:
        lastEnd = result[-1][1]
        if start <= lastEnd:
            result[-1][1] = max(end,lastEnd)
        else:
            result.append([start,end])
    return result

# Number 3: Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, 
# which could point to any node in the list, or null.
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

    def copy(head):
        hashmap = {None: None}
        current = head

        while current:
            copy = Node(current.val)
            hashmap[current] = copy
            current = current.next

        current = head

        while current:
            copy = hashmap[current]
            copy.next = hashmap[current.next]
            copy.random = hashmap[current.random]
            current = current.next

        return hashmap[head]


# Number 3: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def FindMinimum(nums):
    l,r = 0,len(nums) - 1
    result = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result,nums[l])
            break

        mid = (l + r) // 2
        result = min(result,nums[mid])

        # if in left sorted portion
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return result

# Number 4: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time.

def longest(nums):
    numsSet = set(nums)
    count = 0

    for x in numsSet:
        if x -1 not in numsSet:
            longest = 1
        while x + longest in numsSet:
            longest += 1
        count = max(count,longest)

    return count

# Number 5: Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
def isValid(board):
    rows = defaultdict(set())
    cols = defaultdict(set())
    squares = defaultdict(set())

    for r in range(len(board)):
        for c in range(len(board[0])):

            if board[r][c] == ".":
                continue

            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3][c//3]:
                return False
            else:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

    return True