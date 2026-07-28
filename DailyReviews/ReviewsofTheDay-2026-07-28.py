# Number 1: Koko Eating bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

import math
def kokoEatingBananas(piles,h):
    l,r = 1,max(piles)
    result = r

    while l <= r:
        mid = (l + r) // 2
        
        hours = 0
        for p in piles:
            hours += math.ceil(float(p)/mid)

        if hours <= h:
            result = min(result, mid)
            r = mid - 1
        else:
            l = mid + 1

    return result

# Number 2: Binary Search
# Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
# You must write an algorithm with `O(log n)` runtime complexity.

def binarySearch(nums,target):
    l,r = 0,len(nums) -1

    while l<= r:
        mid = (l + (r-l)) / 2

        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            return mid

    return -1

# Number 3: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.  

def validParentheses(s):
    stack = []
    bracketsHash = {"]":"[","}":"{",")":"("}

    for x in s:
        if x in bracketsHash:
            if stack and stack[-1] == bracketsHash[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)

    if stack:
        return False

    return True
        
