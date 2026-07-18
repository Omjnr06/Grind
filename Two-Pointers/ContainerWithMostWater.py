#you are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(height):
    l,r = 0, len(height) - 1
    result = 0

    while l < r:
        area = min(height[l],height[r]) * (r-l)
        result = max(result,area)
        if height[l] < height[r]:
            l += 1
        else:
            r-= 1
    return result