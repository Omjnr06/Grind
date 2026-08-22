# Number 1: Trappin Rainwater
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

def trapping(heights):
    l,r = 0, len(heights) - 1
    leftMax = heights[l]
    rightMax = heights[r]
    result = 0

    if not heights:
        return 0

    while l < r:
        if heights[l] < heights[r]:
            l += 1
            leftMax = max(leftMax,heights[l])
            result += leftMax - heights[l]
        else:
            r -= 1
            rightMax = max(rightMax,heights[r])
            result += rightMax - heights[r]

    return result

#  Number 2: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isCycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

# Number 3: Reverse a Linked List:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverse(head):
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

# Number 4: Container with Most Water
# You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return *the maximum amount of water a container can store*.
# **Notice** that you may not slant the container.

def containerWithMostWater(heights):
    l,r = 0, len(heights) - 1
    maxArea = 0

    while l < r:
        currArea = min(heights[l],heights[r]) * (r-l)
        maxArea = max(maxArea,currArea)
        if heights[l] < heights[r]:
             l += 1
        else:
            r -= 1

    return maxArea

# Number 5: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reorder(head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        secondHalf = slow.next
        prev = None

        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp

        firstHalf = head
        secondHalf = prev

        while secondHalf:
            temp1,temp2 = firstHalf.next,secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return