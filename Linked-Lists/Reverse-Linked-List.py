# Given the head of a singly linked list, reverse the list, and return the reversed list.

def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev
