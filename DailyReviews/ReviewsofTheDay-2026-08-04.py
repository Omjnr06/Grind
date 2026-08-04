# Number 1: Merge 2 Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge(list1,list2):
        dummy = ListNode()
        current = dummy
        while list1 and list2:
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


# Number 2 Time based key value store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.
    
class Timestamp:
    def __init__(self):
        self.store = {}

    def set(key,value,timestamp,self):
        if key not in self.store:
            self.store[key] = [[value,timestamp]]
        self.store[key].append([value,timestamp])

    def get(key,timestamp,self):
        values = self.store.get(key,[])
        l,r = 0,len(values) - 1
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if values[mid] <= timestamp:
                result = values[mid][0]
                l = mid + 1

            else:
                r = mid + 1

        return result  

# Number 3: Find minimum in rotated sorted array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def minimum(nums):
    l,r = 0, len(nums) -1
    result = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result,nums[l])
            break

        mid = (l + r) // 2
        result = min(result,nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1

        else:
            r = mid - 1

    return result


# Number 4: Binary Search
# Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
# You must write an algorithm with `O(log n)` runtime complexity.

def binarySearch (nums, target):
    l,r = 0,len(nums) -1

    if not nums:
        return -1

    while l <= r:
        mid = (l + (r-1) )// 2 

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1

# Number 5: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    stack = []
    bracketsHash = {"]":"[", ")" : "(", "}" : "{"}

    for x in range(len(s)):
        if s[x] in bracketsHash:
            if stack and stack[-1] == bracketsHash[x]:
                stack.pop()

            else:
                return False

        else:
            stack.append(s[x])


    if stack:
        return False

    return True