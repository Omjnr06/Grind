# Number 1: Search a 2D Matrix
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*
# You must write a solution in `O(log(m * n))` time complexity.

def search2dMatrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1

    while top <= bottom:
        midRow = (top + bottom) // 2

        if  target > matrix[midRow][cols - 1]:
            top = midRow + 1

        elif target < matrix[midRow][0]:
            bottom = midRow - 1

        else:
            break

    if not(top <= bottom):
        return False

    row = (top + bottom )// 2
    l,r = 0,len(row) - 1

    while l <= r:
        mid = (l + r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1

        else:
            return True

    return False 

# Number 2: Valid Parentheses
# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    stack = []
    bracketsHash = {"]":"[","}":"{",")":"("}
    for x in s:
        if x in bracketsHash:
            if stack and bracketsHash[x] == stack[-1]:
                stack.pop()
            else:
                return False

        else:
            stack.append(x)

    if stack:
        return False

    return True


# Number 3: Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productOfArray(nums):
    result = [1] * len(nums)

    prefix = 1
    for x in range(len(nums)):
        result[x] = prefix
        prefix *= nums[x]

    postfix = 1
    for x in range(len(nums)- 1, -1, -1):
        result[x] *= postfix
        postfix *= nums[x]

    return result 

# Number 4: Balanced BST
# Given a binary tree, determine if it is height-balanced

class TreeNode:
    def __init__(self,left,right,val):
        self.val = val
        self.left = left
        self.right = right

    def isBalancedBST(root):
        def dfs(node):
            
            if not node:
                return [True,0]

            left,right = dfs(node.left),dfs(node.right)
            isBalanced = ((left[0] and right[0]) and (abs(left[1] - right[1]) <= 1))

            return [isBalanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]

# Number 5: Diameter of BST
# Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.
# The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
# The **length** of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self,right,left,val):
        self.val = val
        self.left = left
        self.right = right

    def diameterOfBST(self,root):
        self.result = 0
        def dfs(node):
            if not node:
                return 0

            left,right = dfs(node.left),dfs(node.right)
            self.result = max(self.result,left + right)

            return 1 + max(left,right)

        dfs(root)
        return self.result

# Number 6: Same Tree
# Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self,right,left,val):
        self.right = right
        self.left = left
        self.val = val

    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if q.val != p.val:
            return False

        return (self.isSame(p.left,q.left) and self.isSame(p.right,q.right))

# Number 7: Course Schedule
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSchedule(prerequisites,numCourses):
    
    adjList = {x:[] for x in range(numCourses)}

    for course,prereq in prerequisites:
        adjList[course] = prereq

    visiting = set()

    def dfs(course):
        if course in visiting:
            return False

        if adjList[course] == []:
            return True

        visiting.add(course)

        for prereq in adjList[course]:
            if not dfs(prereq):
                return False

        adjList[course] = []
        visiting.remove(course)
        return True

    for x in range(numCourses):
        if not dfs(x):
            return False

    return True

# Number 8: Remove nth node from end of list
# Given the head of a linked list, 
# remove the nth node from the end of the list and return its head

class Node:
    def __init__(self,next,random):
        self.next = next
        self.random = random

    def remove(head,n):
        dummy = Node(0,head)
        slow = dummy
        fast = head

        while fast and n > 0:
            fast = fast.next
            n-= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

# Number 9: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self,next,random):
        self.next = next
        self.random = random

    def reorder(head):
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

        firstHalf,secondHalf = head, prev

        while secondHalf:
            temp1,temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2

        return 

# Number 10: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

class Node:
    def __init__(self,next,random):
        self.next = next
        self.random = random

    def linkedListCycle(head):
        slow,fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return False

        return True

# Number 11: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def searchInSorted(nums,target):
    l,r = 0,len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1

# Number 12: Largest Rectangle in Histogram
# Given an array of integers heights representing the 
# histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram. 

def largestRectangle(heights):
    stack = []
    result = 0

    for x in range(len(heights)):
        start = x 

        while stack and stack[x][1] > heights[x]:
            index,height = stack.pop()
            result = max(result, height * (x - index))
            start = index

        stack.append(start,heights[x])

    for i,h in stack:
        result = max(result, h * (len(stack) - i))

    return result