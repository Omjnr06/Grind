

def ValidParentheses(s):
	stack = []
	bracketsHashmap = { ")" : "(" , "]" : "[" , "}" :  "{" }

	for x in s:
		if x in bracketsHashmap:
			if stack and stack[-1] == bracketsHashmap[x]:
				stack.pop()
			else:
				return False
		else:
			stack.append(x)
			

	if stack:
		return False

	return True
