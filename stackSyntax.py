# to initialize an empty stack
stack = []

# to push on a stack, you use the append function
x = 2
y = 3
stack.append(x)
stack.append(y)

#remember that a stack is a LIFO structure so last in is first out
# to pop from a stack you use .pop()

stack.pop(y)

# to peek, python does not have a built in function, instead u use -1 indexing on the stack

top_element = stack[-1]

# to check if the stack is empty

if stack:
    print("stack is not empty")

if not stack:
    print("stack is empty")

# to get the length of the stack
length = len(stack)