# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
	def _init_(self):
		self.stack = []
		self.minStack = []
		
	def push(self,x):
		self.stack.append(x)
		if self.minStack:
			x = min(x , self.minStack[-1])
		else:
			x = x
		self.minStack.append(x)
		
	def pop(self):
		self.stack.pop()
		self.minStack.pop()
		
	def top(self):
		return self.stack[-1]
		
	def getMin(self):
		return self.minStack[-1]
