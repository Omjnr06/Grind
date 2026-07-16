# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):

        if x > 0 and nums[x] == nums[x -1]:
            continue
        l = x + 1
        r = len(nums) - 1

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
                    l +=1
    
    return result
