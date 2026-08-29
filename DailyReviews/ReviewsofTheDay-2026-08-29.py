# Number 1: Trapping Rainwater
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#  compute how much water it can trap after raining.

def trapping(heights):
    l,r = 0, len(heights) - 1
    leftMax = heights[l]
    rightMax = heights[r]
    result = 0

    if not heights:
        return 0
    
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax,heights[l])
            result += leftMax - heights[l]

        else:
             r -= 1
             rightMax = max(rightMax,heights[r])
             result += rightMax - heights[r]

    return result 

# Number 2: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def cycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
