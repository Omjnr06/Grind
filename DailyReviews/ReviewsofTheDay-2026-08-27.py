# Number 1: Number of Islands
# Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
# An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

def numberofIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == "0" or (r,c) in visited:
            return

        visited.add((r,c))

        dfs(r + 1,c)
        dfs(r - 1 ,c)
        dfs(r,c + 1)
        dfs(r,c - 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row,col) not in visited:
                islands += 1
                dfs(row,col)

    return islands

# Number 2: Remove Nth Node from List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def remove(head,n):
        dummy = Node(0,head)
        slow = dummy
        fast = head

        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next 

# Number 3: Median of 2 sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)). 

def median(nums1,nums2):
    A,B = nums1,nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A,B = B,A

    l,r = 0,len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) <= len(A) else float("infinity")
        Bleft = B[j] if j > 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) <= len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft) / 2)
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

    return

# Number 4: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the
#  ith day to get a warmer temperature. If there is no future day for which this is possible, 
# keep answer[i] == 0 instead.

def daily(temperatures):
    result = [0] * len(temperatures)
    stack = [] # index

    for x in range(len(temperatures)):
        while stack and temperatures[x] > temperatures[stack[-1]]:
            index = stack.pop()
            result[x] = x - index
        stack.append(x)

    return result

# Number 5: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

def valid(s):
    bracketsHash = {"]":"[","}":"{",")":"("}
    stack = []

    for x in s:
        if x in bracketsHash:
            if stack and stack[-1] != bracketsHash[x]:
                return False
            else:
                stack.pop()
        else:
            stack.append(s[x])

    return True