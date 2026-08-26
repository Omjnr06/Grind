# Number 1:Best Time to uy and Sell Stock
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def profitchecker(prices):
    l,r = 0,1 # l = buying, r = selling
    maxP = 0

    for x in range(len(prices)):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1

    return maxP

# Number 2: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def mergeIntervals(intervals):
    # interval each element has two elements sort b first
    intervals.sort(key= lambda i:i[0])
    result = [intervals[0]]

    for start,end in intervals:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(start,lastEnd)
        else:
            result.append([start,end])

    return result

# Number 3: Copy List with Random Pointer
# Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.
# For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.
# Return *the head of the copied linked list*.
# The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
# - `val`: an integer representing `Node.val`
# - `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.
# Your code will **only** be given the `head` of the original linked list

class Node:
    def init(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def copy(head):
        # Original to Copy 
        hashmap = {None: None}
        current = head

        while current:
            copy = Node(val = current.val)
            hashmap[current] = copy
            current = current.next

        current = head

        while current:
            copy = hashmap[current]
            copy.next = hashmap[current.next]
            copy.random = hashmap[current.random]
            current = current.next

        return hashmap[head]

# Number 4: Find Minimum in Rotated Sorted Array
# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.
# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.
# You must write an algorithm that runs in `O(log n) time`.

def rotated(nums):
    l,r = 0,len(nums) -1
    result = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result, nums[l])
            break

        mid = (l + r) // 2
        result = min(result, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1

        else:
            r = mid - 1

    return result
