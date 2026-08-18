# Number 1: Remove Nth Node from List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def removenth(head,n):
        dummy = Node(0,head)
        left = dummy 
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

# Number 2: Merge 2 Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def merge(list1,list2):
        dummy = Node()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

# Number 3: Time Basde Key Value STore
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

class Timestamp:
    def __init__(self):
        self.store = {} # key:value [value,timestamp]

    def set(self,key,value,timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self,key,timestamp):
        values = self.store.get(key,[])
        l,r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1

            else:
                r = mid - 1

        return result  

# Number 4: Postfix Notation
# You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return *an integer that represents the value of the expression*.

def RPN(tokens):
    stack = []

    for x in tokens:
        if x == "+":
            stack.append(stack.pop() + stack.pop())
        elif x == "-":
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        elif x == "*":
            stack.append(stack.pop() * stack.pop())
        elif x == "/":
            a,b = stack.pop(),stack.pop()
            stack.append(int(float(b)/a))

        else:
            stack.append(int(x))

    return stack[0]