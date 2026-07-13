# Number 1: Contains Duplicates
# Given an integer array nums return true if any value appears at least twice in the array, and return false otherwise

def ContainsDuplicates(nums):
    seenCharacters = set()

    for x in nums:
        if x in seenCharacters:
            return True
        seenCharacters.add(x)
    
    return False

# Number 2: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and return false otherwise

def ValidAnagram(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Number 3: Two Sum:
# Given an array and a target return the indices of the two numbers such that they add up to target

def TwoSum(target, nums):
    hashmap = {}

    for x in range(len(nums)):
        difference = target - nums[x]
        if difference in hashmap:
            return [x,hashmap[difference]]
        hashmap[nums[x]] = x
    return 
