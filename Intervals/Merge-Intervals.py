# Given an array of intervals where intervals[i] = [starti, endi],
#  merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key= lambda i: i[0]) #sorting by start 
    result = [intervals[0]]

    for start, end in intervals:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(lastEnd,end)
        else:
            result.append([start,end])

    return result
