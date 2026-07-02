#Number 1: Product of the Array Except Itself
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def ProductofArray(array):
    result = [1] * (len(array))

    prefix = 1
    for x in range(len(array)):
        result[x] = prefix
        prefix *= array[x]

    postfix = 1
    for x in range(len(array)-1,-1,-1):
        result *= postfix
        postfix *= array[x]

    return result


# Number 2: PostFix Notation
# You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return *an integer that represents the value of the expression*.

# **Note** that:

# - The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
# - Each operand may be an integer or another expression.
# - The division between two integers always **truncates toward zero**.
# - There will not be any division by zero.
# - The input represents a valid arithmetic expression in a reverse polish notation.
# - The answer and all the intermediate calculations can be represented in a **32-bit** integer.

def RPN(tokens):
    stack = []

    for x in tokens:
        if x == "*":
            stack.append(stack.pop() * stack.pop())
        elif x == "+":
            stack.append(stack.pop() + stack.pop())

        elif x == "-":
            a,b = stack.pop(), stack.pop()
            stack.append(b-a)

        elif x == "/":
            a,b = stack.pop(), stack.pop()
            stack.append(int(float(b)/a))
        
            
        else:
            stack.append(int(x))

    return stack[0]


# Number 3: Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
def topKFreqElements(nums,k):
    hashmap = {}
    result = []

    for x in range(len(nums)):
        hashmap[x] = 1 + hashmap.get(x, 0)
    
    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap,(hashmap[x],x))

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result