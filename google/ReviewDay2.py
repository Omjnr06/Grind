# Number 1: Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# needs work, struggled on it a bit.
# I first sort the array and create a resulting array
# then we create the outer for loop which was our k pointer. 
# a very important clause is that the solution set must not have any duplicates.
# we make sure x > 0 and that the number at x is not the same as the number before it. If it is we just continue
# we set our left pointer to be 1 + the for loop pointer
# we set the right pointer to be the length of the string
# then we do a standard 2 pointer approach we loop while l < r
# we then calculate the threesum values at the curr index (nums[l] + nums[r] + nums[x])
# then if the threesum value is > 0 we increase the left pointer.
#  if the threesum value is < 0 we reduce the right pointer
# else we add the 3 numbers because it means they sum to 0 and we move only the left pointer to 1
# then after we check while the left < right and if the numebr at the left pointer is the same as the numeber previous to it we keeep incrementing left pointer.
def threeSum(nums):
    nums.sort()
    result = []

    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x-1]:
            continue

        l = x + 1
        r = len(nums) - 1

        while l < r:
            threesum = nums[l] + nums[r] + nums[x]
            if threesum > 0:
                l += 1
            elif threesum > 0:
                r -= 1
            else:
                result.append([nums[l],nums[r],nums[x]])
                l += 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1

        return result

