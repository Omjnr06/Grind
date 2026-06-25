# Given two strings s and t, return true if t is an anagram of s, and return false otherwise

def ValidAnagram(s,t):

	if len(s) != len(t):
		return False

	return sorted(t) == sorted(s)
