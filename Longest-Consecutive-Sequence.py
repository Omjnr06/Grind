# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

# You must write an algorithm that runs in `O(n)` time.
def ConsecutiveSequence(nums):

	numsHash = set(nums)
	count = 0

	for x in numsHash:
		if x-1  not in numsHash:
			length = 1
		while x + length in numsHash:
			length += 1
		
		count = max(count, length)
		
	return count
