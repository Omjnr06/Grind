# Number 1: Median of 2 Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def median(nums1,nums2):
    total = len(nums1) + len(nums2)
    half = total // 2
    A,B = nums1,nums2


    if len(B) < len(A):
        A,B = B,A

    l,r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-infinity")
        Aright = A[i+1] if (i + 1) > len(A) else float("infinity")
        Bleft = B[j] if j > 0 else float("-infinity")
        Bright = B[j+1] if (j + 1) > len(B) else float("infinity")

        if Aleft < Bright and Bleft < Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft) / 2)

        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
    return

# Number 2: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait 
# after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
def daily(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for x in range(len(temperatures)):
        while stack and temperatures[x] > temperatures[stack[-1]]:
            index = stack.pop()
            result[x] = x - index
        stack.append(x)

    return result

#  Number 3: Contains Duplicates
# Given an integer array nums return true if any value appears at least twice in the array,
#  and return false otherwise

def contains(nums):
    seen = set()

    for x in nums:
        if x in seen:
            return False
        seen.add(x)

    return True

# Number 4: Valid Anagram:
# Given two strings s and t, return true if t is an anagram of s, and return false otherwise

def isValid(s,t):
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# Number 5: TwoSum 
# Given an array and a target return the indices of the two numbers such that they add up to target

def twoSum(nums,target):
    hashmap = {}

    for x in range(len(nums)):
        difference = target - nums[x]
        if difference in hashmap:
            return [hashmap[difference],x]
        hashmap[nums[x]] = x

    return

