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
        
        



    