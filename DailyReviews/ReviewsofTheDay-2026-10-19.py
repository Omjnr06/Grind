# Number 1: Course Schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSchedule(numCourses,prerequisites):

    adjList = {i:[] for i in range(numCourses)}
    visiting = set()

    for course, prereq in prerequisites:
        adjList[course].append(prereq)

    def dfs(course):
        # base case 1: the course were on in visiting already = loop and prereq cannot be solve
        if course in visiting:
            return False

        # Base case 2: the course list is empty meaning all prereqs have already been completed
        if adjList[course] == []:
            return True

        visiting.add(course)

        for prereqs in adjList[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)
        adjList[course] = []
        return True

    for x in range(numCourses):
        if not dfs(x):
            return False

    return True

# Number 2: Remove Nth Node from end of the list
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self, next, val):
        self.next = next
        self.val = val

    def removeNth(head,n):
        dummy = Node(head,0)
        slow = dummy
        fast = head

        while fast and n> 0:
            fast = fast.next
            n -=1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

# Number 3: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self, next, val):
        self.next = next
        self.val = val

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

        secondHalf = prev
        firstHalf = head

        while secondHalf:
            temp1,temp2 = firstHalf.next,secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return head

# Number 4: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

class Node:
    def __init__(self, next, val):
        self.next = next
        self.val = val

    def linkedListCycle(head):
        fast,slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return False

        return True

# Number 5: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


def searchInRotated(nums,target):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > nums[l]:
            if target < nums[l] or target > nums[mid]:
                l = mid + 1
            else:
                 r = mid - 1 
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

    return -1

# Number 6: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def largestRectangle(heights):
    stack = [] # index,height
    result = 0

    for x in range(len(heights)):
        start = x

        while stack and stack[x][1] > heights[x]:
            index,height = stack.pop()
            result = max(result, height * (x - index))
            start = index

        stack.append([start,heights[x]])

    for i,h in stack:
        result = max(result, h * (len(stack) - h))


    return result

