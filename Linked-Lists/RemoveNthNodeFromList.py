# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def remove(head,n):
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.nex
            n -= 1

        while right:
            right = right.next
            left = left.next 

        left.next = left.next.next

        return dummy.next

