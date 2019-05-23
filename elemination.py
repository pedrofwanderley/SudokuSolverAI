#String representation
#Super easy grids
board_se_01 = '67...15.92...9..149.1.3.2.7..7..48...62.7839.58.2..476.2..4.165.56.8.943.943...28'
board_se_02 = '.2.935..8.8627.5..935.461.77.1.6.28.358.......6.518.7987.6.2..1..91..7..512.9..36'
board_se_03 = '23...176.....8.43.1.65...9.3276.9.8.581.3..2..9.1283..9.2317.4....86527....942613'
board_se_04 = '..49....6.96..427.2831....4......7253.72.984142...5.93..9521..77.569318.6..84.53.'

# Helper function - creates dictionary from string representation
def create_dict_representation(board_s, rows, cols):
    possible_comb = [r+c for r in rows for c in cols]
    board_d = {p:b for b, p in zip(board_s, possible_comb)}
    return board_d

rows = "ABCDEFGHI"
cols = "123456789"
dict_board = create_dict_representation(board_se_02, rows, cols)


board = dict_board

# Helper function - Make a string with the missing elements of a block
def missing_elements(rows, cols):
	missing_elements = '123456789'
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if (board[position] in '123456789'):
			missing_elements = missing_elements.replace(board[position], '')

	return missing_elements	


# Helper function - fills the cells of a block that are with a dot for the possibles elements left
def fill_block_dot_cells(board, rows, cols):
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if board[position] == '.':
			board[position] = missing_elements(rows, cols)

# Helper function - fills all the cells that are with dot for the possibles elements left in the block
def fill_all_dot_cells(board):
	rows = ['ABC', 'DEF', 'GHI']
	cols = ['123', '456', '789']
	for r in rows:
		for c in cols:
			fill_block_dot_cells(board,r,c)

fill_all_dot_cells(board)

#Shows the grid with the blanck spaces fillded with the possibles elements 
print(board)

# Returns a string with the elements that are alone in a row
def row_to_string(board, row):
	cols = '123456789'
	positions = [r+c for r in row for c in cols]
	row_string =''
	for position in positions:
		if (len(board[position]) == 1):
			row_string += board[position]
	return row_string

# Returns a string with the elements that are alone in a colum
def col_to_string(board, col):
	rows = 'ABCDEFGHI'
	positions = [r+c for r in rows for c in col]
	col_string =''
	for position in positions:
		if (len(board[position]) == 1):
			col_string += board[position]
	return col_string

print(row_to_string(board, 'A'))
print(col_to_string(board, '1'))
