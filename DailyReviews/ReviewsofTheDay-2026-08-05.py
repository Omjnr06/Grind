# Number 1: Linked List Cycle:
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

class ListNode:
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


# Number 2: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
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

# Number 3: Median of 2 sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def median(nums1,nums2):
    total = len(nums1) + len(nums2)
    half = total // 2

    A,B = nums1,nums2

    if len(B) < len(A):
        A,B = B,A

    l,r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i > 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float ("infinity")
        Bleft = B[j] if j > 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float ("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min (Aright,Bright)
            else:
                return (min(Aright,Bright) + max(Aleft,Bleft)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

    return


# Number 4: DAily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemps(nums):
    stack = []
    result = [0] * len(nums)

    for x in range(len(nums)):
        while stack and nums[x] > nums[stack[-1]]:
            index = stack.pop()
            result[x] = x - index

        stack.append(x)

    return result

