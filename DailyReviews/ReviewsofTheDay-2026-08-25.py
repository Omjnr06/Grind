# Number 1: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maximumSub(nums):
    maxSub = nums[0]
    currentSum = 0

    for x in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += x
        maxSub = max(maxSub,currentSum)

    return maxSub

# Number 2: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

    def reorder(head):
        fast = head.next
        slow = head

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
            temp1,temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return

# Number 3: Merge 2 Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Node:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

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

# Number 4: Time Based Key Store Value
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self,key,value,timestamp):
        if key not in self.store:
            self.store[key] = [[value,timestamp]]
        else:
            self.store[key].append([value,timestamp])

    def get(self,key,timestamp):
        values = self.store.get(key,[])
        l,r = 0,len(values) - 1
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result

# Number 5: Top K freq Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
def topK(nums,k):
    result = []
    hashmap = {}

    for x in nums:
        hashmap[x] = hashmap.get(x,0) + 1

    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap, (hashmap[x],x))

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap,[1]))

    return result

# Number 6: Group Anagrams
# Given an array of strings, group all the anagrams together. THe answer can be returned in any order

def group(strings):
    hashmap = {}

    for x in range(len(strings)):
        key = "".join(sorted[strings[x]])
        if key in hashmap:
            hashmap[key].append([strings[x]])
        else:
            hashmap[key] = [strings[x]]

    return list(hashmap.values())



                 