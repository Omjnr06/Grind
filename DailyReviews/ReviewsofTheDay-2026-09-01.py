# Number 1: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reorder (head):
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

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
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            secondHalf = temp2
            firstHalf = temp1

        return 

# Number 2: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge(l1,l2):
        dummy = Node()
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next

            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next

# Number 3: Time Based Key Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously,
# with `timestamp_prev <= timestamp`. If there are multiple such values, 
# it returns the value associated with the largest `timestamp_prev`.
#  If there are no values, it returns `""`.

class Timestamp:
    def __init__(self):
        self.store = {}

    def set(self,key,value,timestamp):
        if key not in self.store:
            self.store[key] = [[value,timestamp]]
        else:
            self.store[key].append([value,timestamp])

    def get(self,key,timestamp):
        values = self.store.get(key,[])
        result = ""
        l,r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result  