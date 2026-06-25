# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
from collections import defaultdict


def ValidSudoku(board):
	rows = defaultdict(set())
	cols = defaultdict(set())
	squares = rows = defaultdict(set())

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
			
