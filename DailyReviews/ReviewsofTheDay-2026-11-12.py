# Number 1: Course Schedule 
# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSchedule(numCourses,prerequisites):
    
    adjList = {x:[] for x in range(len(numCourses))}
    visiting = set()

    for c,p in prerequisites:
        adjList[c].append(p)

    def dfs(course):
        if adjList[course] == []:
            return True

        if course in visiting:
            return False

        visiting.add(course)

        for prereq in adjList[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)
        adjList[course] = []
        return True

    for x in range(numCourses):
        if not dfs(x):
            return False


    return True

# Number 2: Number of Islands
# Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
# An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#  You may assume all four edges of the grid are all surrounded by water.

def numberOfIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0 

        if grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r , c + 1)
        dfs(r, c - 1)


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                islands += 1
                dfs(r,c)

    return islands

# Number 3: Remove Nth Node from End of List
# Given the head of a linked list, 
# remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

    def remove(head,n):
        dummy = Node(head)
        fast = head
        slow = dummy

        while fast and n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
        

# Number 4: Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

    def reorder(head):
        slow = head
        fast = head.next


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow
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

# Number 5: Linked List Cycle
# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
# Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

    def isCycle(head):
        slow,fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return False


        return True

# Number 6: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums,target):
    l,r = 0, len(nums) - 1

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

# Number 7: Largest Rectangle in Histogram
# Given an array of integers heights representing the  histogram's bar height where the width of each bar is 1,
#  return the area of the largest rectangle in the histogram.

def largestRectangle(heights):
    stack = []
    result = 0

    for x in range(len(heights)):
        start = x

        while stack and stack[x][1] > heights[x]:
            index, height = stack.pop()
            result = max(result, height * (x - index))
            start = index

        stack.append(start,heights[x])

    for i,h in stack:
        result = max(result, h * (len(stack) - i))

    return result

# Number 8: Balanced BST
# Given a binary tree, determine if it is height-balanced.

class TreeNode:
    def __init__(self,left,right,val):
        self.left = left
        self.right = right
        self.val = val

    def isBalanced(root):

        def dfs(node):

            if not node:
                return [True,0]
            
            left, right = dfs(node.left), dfs(node.right)
            balanced = ((left[0] and right[0]) and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]

# Number 9: Diameter of a Binary Search Tree
# Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.
# The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
# The **length** of a path between two nodes is represented by the number of edges between them.

def diameter(self,root):
    
    self.result = 0

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        self.result = max(self.result, left + right)

        return 1 + max(left,right)

    dfs(root)
    return self.result

# Number 10: Same Tree
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

# Number 11: Postfix Notation
# You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return *an integer that represents the value of the expression*.
# **Note** that:
# - The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
# - Each operand may be an integer or another expression.
# - The division between two integers always **truncates toward zero**.
# - There will not be any division by zero.
# - The input represents a valid arithmetic expression in a reverse polish notation.
# - The answer and all the intermediate calculations can be represented in a **32-bit** integer.

def RPN(tokens):
    stack = []

    for x in tokens:
        if x == "+":
            stack.append(stack.pop() + stack.pop())
        elif x == "-":
            A,B = stack.pop(),stack.pop()
            stack.append(B - A)

        elif x == "*":
            stack.append(stack.pop() * stack.pop())

        elif x == "/":
            A,B = stack.pop(), stack.pop()
            stack.append(int(float(B)/A))

        else:
            stack.append(int(x))

    return stack[0]



        