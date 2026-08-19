# Number 1: Copy List with Random Pointer
# A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.
# Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.
# For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.
# Return *the head of the copied linked list*.
# The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
# - `val`: an integer representing `Node.val`
# - `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.
# Your code will **only** be given the `head` of the original linked list.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def copy(head):
        hashmap = {}
        dummy = head
        current = dummy
        while current:
            copy = Node(current.val)
            hashmap[current] = copy
            current = current.next

        current = dummy

        while current:
            copy = hashmap[current]
            copy.next = hashmap[current.next]
            copy.random = hashmap[current.random]
            current = current.next

        return hashmap[head]

# Number 2: Reorder List
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
        # find middle point, use fast and slow pointer method
        # reverse second half after middle point
        # attach new points

        fast = head.next
        slow = head

        while fast.next:
            slow = slow.next 
            fast = fast.next.next

        secondHalf = slow.next
        prev = None

        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp

        secondHalf = prev
        firstHalf = head

        while secondHalf:
            temp1,temp2 = firstHalf.next,secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return head

# Number 3: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def minimum(nums):
    l,r = 0,len(nums) -1 
    result = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result,nums[l])
            break 

        mid = (l + r) // 2
        result = min(result,nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1

        else:
            r = mid - 1


