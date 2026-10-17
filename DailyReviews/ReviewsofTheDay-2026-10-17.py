# Number 1: Jump Game
# You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.
# Return `true` *if you can reach the last index, or* `false` *otherwise*.

def jumpGame(nums):
    goal = len(nums) -1

    for x in range(len(nums) -2,-1,-1):
        if x + nums[x] >= goal:
            goal = x

    if goal == 0:
        return True

    return False

# Number 2: Max Chunks to Sort
# You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.
# We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return *the largest number of chunks we can make to sort the array*.

def maxChunksToSort(arr):
    chunks = 0
    maxVal = 0

    for x in range(len(arr)):

        maxVal = max(maxVal, arr[x])
        if maxVal == x:
            chunks += 1

    return chunks


# Number 3: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def longestCharacterReplacement(s: str,k: int) -> int:
    l = 0
    count = 0
    hashmap = {}

    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r],0)

        while (r-l+1) - max(hashmap.values()) > k:
            hashmap[s[l]] -= 1
            l += 1

        count = max(count,r-l+1)

    return count 

# Number 4: Longest Substring without any Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(s: str) -> int:
    slidingWindowVals = set()
    l = 0
    count = 0

    for r in range(len(s)):
        if s[r] in slidingWindowVals:
            slidingWindowVals.remove(s[l])
            l += 1

        slidingWindowVals.add(s[r])
        count = max(count,r - l + 1)

    return count
