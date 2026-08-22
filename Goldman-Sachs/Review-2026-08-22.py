#  Number 1: Best Time to Buy and Sell
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
# Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

def best(prices):
    l,r = 0,1 # l = buy, r = sell
    maxProfit = 0

    for p in len(range(prices)):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit,profit)
        else:
            l = r
        r += 1

    return maxProfit

# Number 2: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key= lambda i: i[0])
    result = []

    for start,end in intervals:
        if start <= result[-1][1]:
            result[-1][0] = max(result[-1][1],end)
        else:
            result.append(start,end)

    return result