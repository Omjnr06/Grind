# Number 1: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def searchInRotatedSortedArray(nums,target):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] >= nums[l]:
            if nums[mid] < target or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        else:
            if nums[mid] > target or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1

# Number 2: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.
import math
def eating(piles,h):

    l,r = 1, max(piles)
    result = r

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(float(p)/k)

        if hours <= h:
            result = min(result,k)
            r = k - 1
        else:
            l = k + 1
    return result

# Number 3: Valid Palindrome
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

def isPalindrome(self,s):
    l,r = 0,len(s) - 1

    while l < r:
        while l <r and not self.isAlphaNum(s[l]):
            l += 1
        while r > l and not self.isAlphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1

    return True

def isAlphaNum(self,c):
    return(ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9") or ord("A") <= ord(c) <= ord("Z"))


