# Number 1: Search in 2d Matrix
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.
# You must write a solution in `O(log(m * n))` time complexity.

def search(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1

    while top <= bottom:
        midRow = (top + bottom ) // 2

        if target > matrix[midRow][cols-1]:
            top = midRow + 1
        elif target < matrix[midRow][0]:
            bottom = midRow - 1
        else:
            break

    if not (top <= bottom):
        return False

    row = (top + bottom) // 2
    l,r = 0,len(row) - 1

    while l <= r:
        mid = (l + r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True
    return False

#  Number 2: Remove Nth Node from List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def remove(head,n):
        dummy = Node(next=head)
        fast = head
        slow = dummy
        while n > 0:
            fast = fast.next
            n -= 1


        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

# Number 3: Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function. 

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,value):
        self.stack.append(value)
        if self.minStack:
            value = min(value, self.minStack[-1])
        else:
            value = value

        self.minStack.append(value)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

# Number 4: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.
import math
def koko(h,piles):
    l,r = 1,max(piles)
    result = l

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(float(p)/k)

        if hours <= h:
            result = min(result,k)
            r = k - 1
        else:
            l = k + 1

    return result

# Number 5: Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list 
# of strings.

def encode(strings):
    result = ""
    for x in strings:
        result += len(x) + "*" + x

    return result

def decode(string):
    result = []
    i = 0

    while i < len(string):
        j = i

        while j != "*":
            j += 1

        length = string[i:j]
        i = j + 1
        j = i + length

        result.append(string[i:j])

        i = j

    return result
        