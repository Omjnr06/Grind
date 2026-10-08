# Number 1: Max Depth of Tree
# Given the `root` of a binary tree, return *its maximum depth*.
# A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def maxDepth(self,root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# Number 2: Invert Tree
# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invert(self,root):

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invert(root.left)
        self.invert(root.right)

        return root


# Number 3: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def add(list1,list2):
        carry = 0
        dummy = Node()
        current = dummy

        while list1 or list2 or carry:
            value1 = list1.value if list1 else 0
            value2 = list2.value if list2 else 0

            value = value1 + value2 + carry
            carry  = value // 10
            value = value % 10 

            current.next = Node(value)

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            current = current.next

        return dummy.next


# Number 4: Remove Nth Node from List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Sturggled a bit might move back to stage 1 tbh
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


    def remove(head,n):
        dummy = Node(0,head)
        slow = dummy
        fast = head

        while fast and n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

# Number 5: Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def median(nums1,nums2):
    A,B = nums1,nums2
    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A,B = B,A

    l,r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-infinity")
        Aright = A[i+1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j > 0 else float("-infinity")
        Bright = B[j+1] if (j + 1) < len(A) else float("infinity")

        if Aleft < Bright and Bleft < Aright:
            if total % 2:
                return min(Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft) / 2)
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1 

    return

# Number 6: Car Fleet
# There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
# You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
# If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.
def carFleet(position,speed,target):
    pairs = sorted(zip(position,speed), reverse = True)
    stack = []

    for p,s in pairs:
        stack.append(float(target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

