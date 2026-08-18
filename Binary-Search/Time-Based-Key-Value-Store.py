# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the `TimeMap` class:
# - `TimeMap()` Initializes the object of the data structure.
# - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
# - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. 
# If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

class TimeStamp:
    def __init__(self):
        self.store = {}

    def set(self,key,value,timestamp):
        if key not in self.store:
            self.store[key] = []    
        self.store[key].append([value,timestamp])

    def get(self,key,timestamp):
        result = ""
        values = self.store.get(key,[])
        l,r = 0,len(values) -1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result




    