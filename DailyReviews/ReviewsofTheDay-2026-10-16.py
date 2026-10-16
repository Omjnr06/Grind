# Number 1: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key = lambda i:i[0])
    result = [intervals[0]]

    for start,end in intervals:
        lastEnd = result[-1][1]

        if start < lastEnd:
            result[-1][1] = max(lastEnd,end)

        else:
            result.append((start,end))


    return result

# Number 2: Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
def topK(nums,k):
    result = []
    heap = []
    hashmap = {}

    for x in nums:
        hashmap[x] = 1 + hashmap.get(x,0)

    for x in hashmap.keys():
        heapq.heappush(heap, hashmap[x],x)

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap)[1])


    return result

# Number 3: Max Depth of Tree
# Given the `root` of a binary tree, return *its maximum depth*.
# A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self,root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


# Number 4: Invert Tree
# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self,root):
        
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


# Number 5: Add 2 Numbers
# You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node(object):
    def __init__(self: 'Node', next: 'Node' = None, val: int = 0) -> 'Node':
        self.val = val
        self.next = next

    def add(list1,list2):
        carry = 0
        dummy = Node(0,None)
        current = dummy

        while list1 or list2 or carry:
            list1Val = list1.val if list1 else 0
            list2Val = list2.val if list2 else 0

            value = list1Val + list2Val + carry
            carry = value // 10
            value = value % 10 

            current.next = Node(value)

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

            current = current.next

        return dummy.next

# Number 6: Remove Nth Node from End of the list
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node(object):
    def __init__(self: 'Node', next: 'Node' = None, val: int = 0) -> 'Node':
        self.val = val
        self.next = next


    def remove(head,n):
        dummy = Node(0,head)
        fast = head
        slow = head

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next        

# Number 7: Koko Eating Bananas
# Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
# Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

import math
def kokoEating(piles,h):
    l,r = 1, max(piles)
    result = l

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(float(p)/k)

        if hours <= h:
            result = min(result,k)
            r = k - 1

        else:
            l = k + 1

    return result 
