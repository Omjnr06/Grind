# Number 1: Add number
# You are given two **non-empty** linked lists representing two non-negative integers.
#  The digits are stored in **reverse order**, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next


    def add(list1,list2):
        dummy = Node()
        current = dummy
        carry = 0

        while list1 or list2 or carry:
            value1 = list1.val if list1 else 0
            value2 = list2.val if list2 else 0

            value = value1 + value2 + carry
            carry = value // 10
            value = value % 10

            current.next = Node(value)

            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next


# Number 2: Longest Substring without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubString(s):
    characterSet = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in characterSet:
            characterSet.remove(s[l])
            l += 1

        characterSet.add(s[r])

        result = max(result,r - l + 1)

    return result

# Number 3: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSub(nums):
    currentSum = 0
    maxSum = 0

    for x in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += x
        maxSum = max(maxSum,currentSum)

    return maxSum


# Number 4: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def repeatingChars(s,k):
    count = {}
    l = 0
    result = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        
        if ((r - l + 1) - max(count.values())) < k:
            count[s[l]] -= 1
            l += 1

        
        result = max(result, r-l+1)

    return result


# Number 5: Reverse Polish Notation
# You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return *an integer that represents the value of the expression*.

def RPN(tokens):
    stack = []

    for x in tokens:
        if x == "+":
            stack.append(stack.pop() + stack.pop())

        if x == "-":
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        if x == "*":
            stack.append(stack.pop() * stack.pop())

        if x == "/":
            a,b = stack.pop(),stack.pop()
            stack.append(int(float(b)/a))

        else:
            stack.append(int(x))

    return stack[0]


# Number 6: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and return false otherwise

def isValidAnagram(s,t):
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# Number 7: Contains Duplicates
# Given an integer array nums return true if any value appears at least twice in the array, and return false otherwise

def hasDuplicate(nums):
    seen = set()

    for x in nums:
        if x in seen:
            return False
        seen.add(x)

    return True 


# Number 8: Group Anagrams
# Given an array of strings, group all the anagrams together. THe answer can be returned in any order

def groupAnagrams(strings):
    hashmap = {}

    for x in range(len(strings)):
        key = "".join(sorted(strings[x]))
        if key in hashmap:
            hashmap[key].append(strings[x])
        else:
            hashmap[key] = [strings[x]]

    return list(hashmap.values()) 

# Number 9: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.


def isValidParentheses(s):
    stack = []
    bracketsHash = {"]":"[","}":"{",")":"("}

    for x in range(len(s)):
        if x in bracketsHash:
            if stack[-1] != bracketsHash[s[x]]:
                return False
            else:
                stack.pop()

        stack.append(s[x])

    if stack:
        return False

    return True


# Number 10: Search a 2D Matrix
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.
# You must write a solution in `O(log(m * n))` time complexity.

def search2d(target,matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0 
    bottom = rows - 1

    if not matrix:
        return False

    while top <= bottom:
        midRow = (top + bottom) // 2

        if target > matrix[midRow][cols - 1]:
            top = midRow + 1

        elif target < matrix[midRow][0]:
            bottom = midRow - 1

        else:
            break

    if not(top <= bottom):
        return False

    row = (top + bottom) // 2
    l,r = 0, len(row) - 1


    while l <= r:
        mid = (l + r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1

        else:
            return True

    return

