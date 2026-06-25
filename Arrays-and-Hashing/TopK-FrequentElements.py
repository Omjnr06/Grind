# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Proper Solve

import heapq

def TopKFreq(nums,k):


    hashmap = {}
    result = []

    for x in nums:
        if x in hashmap:
            hashmap[x] = 1 + hashmap.get(x, 0)


    heap = []

    for x in hashmap.keys():
        heapq.heappush(heap, (hashmap[x], x))
        
        if(len(heap) > k):
            heapq.heappop(heap)
            
    for x in range(k):
        result.append(heapq.heappop(heap)[1])
        

    return result




# My Initial Solve
##Accepted on leetcode but time and space complexity is not good due to "key = hashmap.get" line
def TopKFreqV2(nums):
        hashmap = {}
        result = []
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        while k > 0:
            max_key = max(hashmap, key=hashmap.get)
            result.append(max_key)
            del hashmap[max_key]
            k = k - 1
        
        return result
