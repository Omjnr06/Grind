# Number 1: Two Sum II - Input Array is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def TwoSumII(nums,target):

    l,r = 0,len(nums) - 1


    while l < r:
        twoSum = nums[l] + nums[r]

        if(twoSum > target):
            r -= 1
        elif (twoSum < target):
            l += 1
        else:
            return [l + 1, r + 1]
        
    return

# Number 2: Trapping Rainwater
# Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

def trappingRainWater(heights):
    l,r = 0, len(heights) - 1
    leftMax,rightMax = heights[l] , heights[r]
    result = 0

    if not heights:
        return 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, heights[l])
            result += leftMax - heights[l]

        else:
            r-= 1
            rightMax = max(rightMax,heights[r])
            result += rightMax - heights[r]

    return result
        
# Number 3: Search a 2D Matrix
# ## 
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.
# You must write a solution in `O(log(m * n))` time complexity.

def search2DMAtrix(matrix, target):
    rows, cols = len(matrix),len(matrix[0])
    top,bottom = 0, cols - 1

    while top <= bottom:
        currentRow = (top + bottom )// 2

        if target > matrix[currentRow][cols -1]:
            top = currentRow + 1
        elif target < matrix[currentRow][0]:
            bottom = currentRow -1
        else:
            break

    if not (top <= bottom):
        return False
    
    l,r = 0, cols - 1
    currentRow = (top + bottom) // 2

    while l <= r:
        mid = (l + r) // 2

        if target > matrix[currentRow][mid]:
            l = mid + 1
        elif target < matrix[currentRow][mid]:
            r = mid - 1
        else:
            return True
        
    return False

# Number 4: Valid Palindrome
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

def validPalindrome(self,s):
    l,r = 0,len(s) -1

    while l < r:

        while l < r and  not self.alphanum(s[l]):
            l +=1
        while r > l and not self.alphanum(s[r]):
             r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        
        l,r = l + 1, r + 1
        
    return True

def alphanum(c):
    return (ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9"))
    


# Number 5: 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def ThreeSum(nums):
    result = []

    for x in range(len(nums)):

        l,r = x + 1, len(nums) - 1

        if x > 0 and nums[x] == nums[x - 1]:
            continue


        while l < r:
            threesum = nums[x] + nums[l] + nums[r] 
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1

            else:
                result.append([nums[x],nums[l],nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return result

# Number 6: Binary Search
# Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
# You must write an algorithm with `O(log n)` runtime complexity.
def BinarySearch(target,nums):
    l,r = 0, len(nums) -1

    while l < r:
        mid = (l + (r-l)) // 2
        if nums[mid] > target:
            r -= 1
        elif nums[mid] < target:
            l += 1
        else:
            return mid
    return -1
