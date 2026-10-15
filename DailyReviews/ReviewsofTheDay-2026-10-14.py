# Number 1: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def characterReplacement(s,k):
    result = 0
    l = 0
    freqList = {}

    for r in range(len(s)):
        freqList[s[r]] = 1 + freqList.get(s[r], 0)

        while (r-l + 1) - max(freqList.values()) > k:
            freqList[s[r]] -= 1
            l += 1

        result = max(result, r-l + 1)

    return result

# Number 2: Longest Substring without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(s):
    seen = set()
    result = 0
    l = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[1])
            l += 1

        seen.add(s[r])
        result = max(result, r - l + 1)

    return result

# Number 3: Median of 2 Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def medianOf2Sorted(nums1,nums2):
    A,B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A,B = B,A

    l,r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j > 0 else float("-infinity")
        Bright = B[j + 1] if (i + 1) < len(B) else float("-infinity")

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

# Number 4: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(target,position,speed):
    pairs = sorted(zip(position,speed), reverse= True)
    stack = []

    for p,s in pairs:

        stack.append(float(target -p)/s)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# Number 5: Jump Game
# You are given an integer array `nums`. You are initially positioned at the array's 
# **first index**, and each element in the array represents your maximum jump length at that position.
# Return `true` *if you can reach the last index, or* `false` *otherwise*.

def jumpGame(nums):
    goal = len(nums) - 1

    for x in range(len(nums) -2 , -1, -1):
        if x + nums[x] >= goal:
            goal = x

    if goal == 0:
        return True

    return False

# Number 6: Max Chunks to Sort
# You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.
# We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return *the largest number of chunks we can make to sort the array*.

def maxChunks(arr):
    chunks = 0
    largest = 0

    for x in range(len(arr)):
        largest = max(largest, arr[x])
        if largest == x:
            chunks += 1

    return chunks

