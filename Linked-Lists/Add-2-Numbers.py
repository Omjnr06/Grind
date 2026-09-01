# You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(list1,list2):
        dummy = Node()
        current = dummy
        carry = 0

        while list1 or list2 or carry:
            list1Val = list1.val if list1 else 0
            list2Val = list2.val if list2 else 0


            value = list1Val + list2Val + carry
            carry = value // 10
            value = value % 10

            current.next = Node(value)

            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next

