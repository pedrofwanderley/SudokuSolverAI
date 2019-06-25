#This file contains the helpers functions that all the others files use

# Helper function - Returns an boolean value, True if all positions have only one value alocated and False otherwise
def check_solution(board, rows, cols):
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if (len(board[position]) > 1):
			return False


	return True  