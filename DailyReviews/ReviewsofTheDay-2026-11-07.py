# Number 1: Longest Repeating Character Replacement
# You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
# Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

def longestCharacter(self,s,k):
    hashmap = {}
    l = 0
    result = 0

    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(hashmap[s[r]],0)

        if (r - l + 1) - max(hashmap.values()) > k:
            hashmap[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result

# Number 2: Merge 2 Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Node:
    def __init__(self,next,val):
        self.val = val
        self.next = next

    def merge2(list1,list2):
        dummy = Node(0,None)
        current = dummy

        while current:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        elif list2:
            current.next = list2

        return dummy.next

# Number 3: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

import math
def kokoEating(piles,h):
    
    l,r = 1, max(piles)
    result = l

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(float(p)/k)

        if hours <= h:
            result = min(result, hours)
            r = k - 1

        else:
            l = k + 1 

    return result

# Number 4: Binary Search
# Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
# You must write an algorithm with `O(log n)` runtime complexity.

def binarySearch(nums,target):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid =  (l + (r-l)) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            r = mid - 1

        else:
            l = mid + 1

    if not (l<=r):
        return -1

# Number 5: Two Sum II: Input Array IS Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSumII(nums,target):
    l,r = 0, len(nums) - 1

    while l < r:
        value = nums[l] + nums[r]
        if value > target:
            r -= 1
        elif value < target:
            l += 1

        else:
            return [l + 1,r + 1]

    if not(l < r):
        return -1

# Number 6: Encode and Decode String
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the 
# original list of strings.

def encode(strings):
    
    result = ""

    for x in strings:
        result += len(x) + "*" + x


    return result

def decode(string):
    result = []
    i = 0

    while i < len(string):
        j = i

        while string[j] != "*":
            j += 1

        length = int(string[i:j])

        i = j + 1
        j = i + length
        word = string[i:j]
        result.append(word)

        i = j

    return result

# Number 7: Top K Frequent Elements
# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

import heapq
def topk(nums,k):
    hashmap = {}
    result = []

    for x in nums:
        hashmap[x] = 1 + hashmap.get(x,0)

    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap,hashmap[x],x)

        if len(heap) > k:
            heapq.heappop(heap)


    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result

# Number 8: Two Sum
# Given an array and a target return the indices of the two numbers such that they add up to target

def twoSum(nums,target):
    hashmap = {}

    for x in range(len(nums)):
        difference = target - nums[x]

        if difference in hashmap:
            return [x,hashmap[difference]]
    
        hashmap[nums[x]] = x

    return -1
