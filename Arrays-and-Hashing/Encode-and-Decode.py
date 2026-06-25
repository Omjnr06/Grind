# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# for encoding:

def encoding(stringArray):
	result = ""

	for words in stringArray:
		result = result + len(words) + "*" + words
	return result

# for decoding

def decoding(s):

	result = []
	k = 0

	while k < len(s):
		j = k
		while s[j] != "*":
			j = j + 1
		length = int(s[k:j])
		k = j + 1
		j = length + k
		result.append(s[k:j])
		k = j

	return result
