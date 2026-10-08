# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


def jumpGame(nums):
    goal = len(nums) - 1

    for x in range(len(nums) -2,-1,-1):
        if x + nums[x] >= goal:
            goal = x

    if goal == 0:
        return True

    return False 