# Number 1: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

def ValidParentheses(s):
    stack = []
    bracketsHash = {"]":"[","}":"{",")":"("}

    for x in s:
        if x in bracketsHash:
            if stack and stack[-1] != bracketsHash[x]:
                return False
            else:
                stack.pop()
        else:
            stack.append(x)
    
    if stack:
        return True
    return False

# Number 2: Longest Rectangle in Histogram
# Given an array of integers heights representing the  
# histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

def LongestRectangleinHistogram(heights):
    maxArea = 0
    stack = []

    for x in range(len(heights)):
        start = x

        while stack and heights[x] < heights[stack[-1]]:
            index, height = stack.pop()
            maxArea = max(maxArea, (height * (x - index)))
            start = index
        stack.append(start,height)

        for i,h in stack:
            maxArea = max(maxArea, h * (len(stack)- i))
        return maxArea
    
