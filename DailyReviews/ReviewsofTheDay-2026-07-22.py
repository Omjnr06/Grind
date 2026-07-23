# Number 1: Container with the Most Water
# You are given an integer array `height` of length `n`. 
# There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(height):
    l,r = 0,len(height) -1
    result = 0

    while l < r:
        area = min(height[l],height[r]) * (r-l)
        result = max(result,area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return result

# Number 2: Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait 
# after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemps(temperatures):
    stack = []
    result = [0] * (len(temperatures))

    for x in range(len(temperatures)):
        while stack and temperatures[x] > temperatures[stack[-1]]:
            currentTemp = stack.pop()
            result[x] = x - currentTemp
        stack.append(x)

    return result


# Number 3: Encode and Decode String
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.

def encode(strings):
    result = ""
    for x in strings:
        result += len(x) + "*" + x
    
    return result


def decode(s):
    result = []
    x = 0

    while x < len(s):
        j = x
        while s[j] != "*":
            j += 1

        length = int(s[x:j])
        x = j + 1
        j = x + length

        result.append(s[x:j])

        x = j
    return result
