# Number 1: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next

    def reorder(head):
        slow = head
        fast = head.next

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

        firstHalf = head
        secondHalf = prev

        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return head

# Number 2: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums,target):
    l,r = 0, len(nums) -1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        # left sorted portion
        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid + 1

        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


# Number 3: Search in a 2D Matrix
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.
# You must write a solution in `O(log(m * n))` time complexity.

def searchin2DMatrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1

    if not matrix:
        return False

    while top <= bottom:
        midRow = (top + bottom) // 2

        if target > matrix[midRow][cols -1]:
            top = midRow + 1
        elif target < matrix[midRow][0]:
            bottom = midRow - 1
        else:
            break

    if not (top <= bottom):
        return False

    row = (top + bottom) // 2
    l,r = 0, len(row) - 1

    while l <= r:
        mid = (l + r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid + 1
        else:
            return True

    return False

