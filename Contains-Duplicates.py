# Given an integer array nums return true if any value appears at least twice in the array, and return false otherwise
def ContainsDuplicates(nums):

    seen_nums= set()

    for num in nums:
        if num in seen_nums:
            return True
        seen_nums.add(num)

    return False
    
