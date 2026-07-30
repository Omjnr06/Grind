# Number 1: Search a 2D Matrix
# You are given an `m x n` integer matrix `matrix` with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.
# You must write a solution in `O(log(m * n))` time complexity.

def search2dMatrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    top,bottom = 0,len(rows) - 1

    if not matrix:
        return False

    while top <= bottom:
        midRow = (top + bottom) // 2

        if target > matrix[midRow][cols -1]:
            top = midRow + 1
        elif target < matrix[midRow][0]:
            bottom = midRow - 1
        else:
            break

    if not(top <= bottom):
        return False

    row = (top + bottom) // 2
    l,r = 0,len(row) - 1

    while l<= r:
        mid = (l + r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return mid

    return False 