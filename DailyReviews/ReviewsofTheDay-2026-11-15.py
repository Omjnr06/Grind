# Number 1: Longest Substring without any Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def longestSubstring(self,s):
    l = 0
    charSet = set()
    result = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        result = max(result, r- l + 1)

    return result


# Number 2: Time Based Key Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, 
# with `timestamp_prev <= timestamp`. If there are multiple such values, 
# it returns the value associated with the largest `timestamp_prev`. If there are no values, 
# it returns `""`.

class Timestamp:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key  not in self.store:
            self.store[key] = []

        self.store.append([value,timestamp])

    def get(self, key, timestamp):
        values = self.store.get(key,[])
        l,r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if timestamp <= values[mid][1]:
                result = values[mid][0]
                l = mid + 1

            else:
                r = mid - 1

        return result

# Number 3: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def mostContainer(self , heights):
    l,r = 0, len(heights) - 1
    result = 0
    while l < r:
        area = min(heights[l],heights[r]) * (r-l)
        result = max(result,area)

        if heights[l] < heights[r]:
            l += 1
        else:
             r -= 1
    return result
