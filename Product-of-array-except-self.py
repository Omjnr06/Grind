# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def ProductofArray(array):
	result = [1] * len(array)

	prefix = 1
	for x in range(len(array)):
		result[x] = prefix
		prefix = prefix * array[x] 
		
	postfix = 1
	for x in range(len(array)-1,-1,-1):
		result[x] *= postfix
		postfix = postfix * array[x]
		
		
	return result
	
