# Number 1: Two Sum II Input Array is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def TwoSumII(nums,target):
    l, r = 0, len(nums) - 1

    while l < r:
        twosum = nums[l] + nums[r]

        if twosum > target:
            r -=1

        elif twosum < target:
            l += 1
        else:
            return [l + 1,r + 1]  
    return

# Number 2: Valid Palindrome
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

def isPalindrome(self,s):
    l,r = 0,len(s) -1

    while l < r:
        while  l < r and not self.isAlphaNum(s[l]):
            l += 1
        while  r > l and not self.isAlphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        else:
            l += 1 
            r -= 1

    return True
            
def isAlphaNum(self,c):
    return (ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9"))


# Number 3: Product of Array except self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productOfArray(nums):
    result = [1] * (len(nums))

    prefix = 1
    for x in range(len(nums)):
        result[x] = prefix
        prefix *= nums[x]


    postfix = 1
    for x in range(len(nums)-1,-1,-1):
        result[x] *= postfix
        postfix *= nums[x]

    return result

# Number 4: Longest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height 
# \where the width of each bar is 1, return the area of the largest rectangle in the histogram

def longestRectangleInHistogram(heights):
    stack = [] # pair of the index and the height
    maxArea = 0

    for x in range(len(heights)):
        start = x
        while stack and heights[x] < heights[stack[-1]]:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (x - index))
            start = index
            
        stack.append((start,heights[x]))

    for i,h in range(stack):
        maxArea = max(maxArea, h * (len(stack) - i))

    return maxArea


