# You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return *an integer that represents the value of the expression*.

def RPN(tokens):
    stack = []

    for x in tokens:

        if x == "+":
            stack.append(stack.pop() + stack.pop())

        elif x == "*":
            stack.append(stack.pop() * stack.pop())

        elif x == "-":
            a,b = stack.pop(), stack.pop()
            stack.append(b-a)

        elif x == "/":
            a,b = stack.pop(),stack.pop()
            stack.append(int(float(b)/a))

        else:
            stack.append(int(x))
    
    return stack[0]

