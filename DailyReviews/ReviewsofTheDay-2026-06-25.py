#  Number 1: Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# remember to import heapq
# create a hashmap and a resulting array
# get a count for each digit
# create the heap and  push all key value pairs in reverse order as set into the heap(value,key)
# only need the top k elements so you can pop the rest from heap
# loop thru length of heap, and append to resulting array the 1th element (because we need the value not the count of the value)

import heapq

def TopK(nums,k):
    hashmap = {}
    result = []

    for x in len(range(nums)):
        
        if nums[x] in hashmap:
            hashmap[x] = 1 + hashmap.get(x,0)
    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap,(hashmap[x],x))

        if len(heap) > k:
            heapq.heappop(heap)

    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result
        
        

# Number 2: Valid Sudoku
# see leetcode for details
# need to import special collection to make a hashmap where value is a set
# create dictionaries where the value is a set()
# 2d loop (loop thru the rows then a column = length of 1 row)
# in leetcode problem it says that te sudoku board doesnt have to be complete. THe incomplete square value is "." so we handle that edge case
# we check if the value we ar eon has been seen in the row it belows to or the column it belongs or the square it belongs to
# if it does return false
# if it hasnt been seen yet add it to each of the respective areas
# if it makes it past the loop then you can return true

from collections import defaultdict
def ValidSudoku(board):
    rows = defaultdict(set())
    cols = defaultdict(set())
    squares = defaultdict(set())

    for r in range(len(board)):
        for c in range(len(board[0])):
            
            if board[r][c] == ".":
                continue

            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])


    return True


# Number 3 Group Anagrams 
# Given an array of strings, group all the anagrams together. THe answer can be returned in any order
# create a hashmap and loop thru the indices of the array.
# create a key as the sorted then restringified version of the current word
# if that key already seen in the array, add the value to the keys list of values
# if the key not in the hashmap, create it as the key value pair being the key as the sorted version and the value being the actual word
# return the listified hashmap.values.

def GroupAnagrams(strings):
    hashmap = {}

    for x in range(len(strings)):
        key = "".join(sorted(strings[x]))
        if key in hashmap:
            hashmap[key].append(strings[x])
        else:
            hashmap[key] = [strings[x]]

    return list(hashmap.values())
    