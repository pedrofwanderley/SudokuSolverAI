import elimination
import only_choice
import grids

# Gri's coordinates
rows = 'ABCDEFGHI'
cols = '123456789'
block_rows = ['ABC', 'DEF', 'GHI']
block_cols = ['123', '456', '789']

# Helper function - creates block string from string representation
def board_string_vizualization(board_string):
	string = ''
	count = 0
	for element in board_string:
		string += element + ' '
		count += 1
		if (count == 9) :
			string += '\n'
			count = 0

	return string

# Helper function - creates dictionary from string representation
def create_dict_representation(board, rows, cols):
    possible_comb = [r+c for r in rows for c in cols]
    map_board = {p:b for b, p in zip(board, possible_comb)}
    return map_board

# Creates a string representation with rows and columns for the board
def board_to_string(board, rows, cols):
	string = ''
	positions = [r+c for r in rows for c in cols]
	count = 0
	for position in positions:
		string += board[position] + ' '
		count += 1
		if (count == 9) :
			string += '\n'
			count = 0

	return string

#To see the elimination technique flow with the board_se_01

print(board_string_vizualization(grids.board_se_01))

board = create_dict_representation(grids.board_se_01, rows, cols)

elimination.fill_all_dot_cells(board, block_rows, block_cols)

print(board_to_string(board,rows,cols))

board_updated = elimination.elimination_technique(board, rows, cols)
print(board_to_string(board_updated, rows, cols))

print('\n>> ---------------------------------- << \n')
