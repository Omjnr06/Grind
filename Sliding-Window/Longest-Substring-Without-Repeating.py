# Given a string s, find the length of the longest substring without duplicate characters.
def longestSubstring(s):
    l = 0
    result = 0
    characterSet = set()

    for r in range(len(s)):
        while s[r] in characterSet:
            characterSet.remove(s[l])
            l += 1

        characterSet.add(s[r])
        result = max(result, r - l + 1)

    return result