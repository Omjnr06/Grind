# Number 1: Two Sum - Input Array is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twosumII(nums,target):
    l,r = 0, len(nums) - 1

    while l < r:
        current = nums[l] + nums[r]
        if current > target:
            r -= 1
        elif current < target:
            l += 1
        else:
            return [l+1, r+1]

    return -1

# Number 2: Two Sum
# Given an array and a target return the indices of the two numbers such that they add up to target
def twoSum(nums,target):
    hashmap = {} #  key: difference  value = index

    for x in range(len(nums)):
        difference = target - nums[x]
        if difference in hashmap:
            return [x,hashmap[difference]]
        else:
            hashmap[nums[x]] = x

    return -1

# Number 3: Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.

class Password:
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
            while string[j] != "*":
                j += 1
            length = int(string[i:j])
            i = j + 1
            j = i + length
            result.append(string[i:j])
            i = j

        return result 

# Number 4: Longest Consecutive Sequence
# Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*
# You must write an algorithm that runs in `O(n)` time

def longestSequence(nums):
    maxLength = 0
    numSet = set(nums)

    for x in numSet:
        if x - 1 not in numSet:
            length = 1
        while x + length in numSet:
            length += 1

        maxLength = max(maxLength,length)

    return maxLength

# Number 5: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

def carFleet(target,position,speed):
    pairs = sorted(zip(position,speed),reverse=True)
    stack = []

    for p,s in pairs:
        stack.append(float((target-p)/(s)))
        if len(stack) >=2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# Number 6: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def longestRectangle(heights):
    stack = [] # index, height
    maxArea = 0

    for x in range(len(heights)):
        start = x
        while stack and stack[x][1] > heights[x]:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (x - index))
            start = index
        stack.append(start, heights[x])

    for i,h in stack:
        maxArea = max(maxArea, h * (len(stack) - i))

    return maxArea


# Number 7: Binary Search 
# Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
# You must write an algorithm with `O(log n)` runtime complexity.

def binary(nums,target):
    l,r = 0,len(nums) - 1

    while l <= r:
        mid =  (l + (r-l) // 2)
        if nums[mid] > target:
            r = mid -1 
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid

    return -1

# Number 8: Median of 2 sorted arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def median2sorted(nums1,nums2):
    total = len(A) + len(B)
    half = total // 2
    A,B = nums1,nums2
    if len(B) < len(A):
        A,B = B,A

    l,r = 0, len(A) - 1

# using while ture here because in question we are promised an answer but could use l <= r method as well
    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j > 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft) / 2)
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

    return

# Number 9: Merge 2 Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

    def merge(list1,list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
            else:
                current.next = list2
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next

# Number 10: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

class Node:
    def __init__(self, val = 0, next = None):
        self.next = next
        self.val = val

    def isCycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Number 11: Remove nth Node from List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def remove(head,n):
        dummy = Node(0,head)
        fast = head
        slow = dummy

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next


        slow.next = slow.next.next

        return dummy.next

# Number 12: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def add(list1,list2):
        dummy = Node()
        current = dummy
        carry = 0

        while list1 and list2 and carry:
            value1 = list1.val if list1 else 0
            value2 = list2.val if list2 else 0

            value = value1 + value2 + carry
            carry = value // 10
            value = value % 10

            current.next = Node(value)
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

            current = current.next

        return dummy.next



