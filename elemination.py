#String representation

#Super Easy Boards
#se = super easy
board_se_01 = '67...15.92...9..149.1.3.2.7..7..48...62.7839.58.2..476.2..4.165.56.8.943.943...28'
board_se_02 = '.2.935..8.8627.5..935.461.77.1.6.28.358.......6.518.7987.6.2..1..91..7..512.9..36'
board_se_03 = '23...176.....8.43.1.65...9.3276.9.8.581.3..2..9.1283..9.2317.4....86527....942613'
board_se_04 = '..49....6.96..427.2831....4......7253.72.984142...5.93..9521..77.569318.6..84.53.'

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


# Helper function - Make a string with the missing elements of a block
def missing_elements(selected_rows, selected_cols):
	missing_elements = '123456789'
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		if (board[position] in '123456789'):
			missing_elements = missing_elements.replace(board[position], '')

	return missing_elements	


# Helper function - fills the cells of a block that are with a dot for the possibles elements left
def fill_block_dot_cells(board, selected_rows, selected_cols):
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		if board[position] == '.':
			board[position] = missing_elements(selected_rows, selected_cols)

# Helper function - fills all the cells that are with dot for the possibles elements left in the block
def fill_all_dot_cells(board, block_rows, block_cols):
	for r in block_rows:
		for c in block_cols:
			fill_block_dot_cells(board,r,c)


# Helper function - Make an array with the missing elements positions
def empty_positions(board, rows, cols):
	positions = [r+c for r in rows for c in cols]
	empty_positions_list = []
	for position in positions:
		if(len(board[position]) != 1):
			empty_positions_list.append(position)
	
	return empty_positions_list


# Returns a string with the elements that are already allocated in a row 
def row_to_string(board, row, cols):
	positions = [r+c for r in row for c in cols]
	row_string =''
	for position in positions:
		if (len(board[position]) == 1):
			row_string += board[position]
	return row_string

# Returns a string with the elements that are already allocated in a colum
def col_to_string(board, col, rows):
	positions = [r+c for r in rows for c in col]
	col_string =''
	for position in positions:
		if (len(board[position]) == 1):
			col_string += board[position]
	return col_string

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

# Eliminates a possible element position that is already in a string (can be a row string or a column string)
def eliminate_peer_in_a_string(missing, allocated):
	for element in missing:
		if (element in allocated):
			missing = missing.replace(element, '')

	return missing

# Eliminates a possible element position that is already in a row or column
def eliminate_peer(board, rows, cols, empty_positions_list):
	#Eliminates possibles elements by rows
	for position in empty_positions_list:
		row_missing = position[0]
		missing_elements = board[position]
		allocated_elements_row = row_to_string(board, row_missing, cols)
		board[position] = eliminate_peer_in_a_string(missing_elements, allocated_elements_row)

	updated_empty_positions_list = empty_positions(board ,rows, cols)

	#Eliminates possibles elements by columns
	for position in updated_empty_positions_list:
		col_missing = position[1]
		missing_elements = board[position]
		allocated_elements_col = col_to_string(board, col_missing, rows)
		board[position] = eliminate_peer_in_a_string(missing_elements, allocated_elements_col)

	return board

# Makes a loop to eliminate all the redundant elements in the grid
def elimination_technique(board, rows, cols):
	empty_positions_list = empty_positions(board,rows, cols)
	while(len(empty_positions_list) > 0):
		board_updated = eliminate_peer(board,rows,cols,empty_positions_list)
		empty_positions_list = empty_positions(board_updated,rows, cols)

	return board_updated

#To see the elimination technique flow with the board_se_01
board = create_dict_representation(board_se_01, rows, cols)

print(board_string_vizualization(board_se_01))

fill_all_dot_cells(board,block_rows, block_cols)

print(board_to_string(board,rows,cols))

board_updated = elimination_technique(board, rows, cols)
print(board_to_string(board_updated, rows, cols))

print('\n>> ---------------------------------- << \n')

#To see the elimination technique flow with the board_se_02
board = create_dict_representation(board_se_02, rows, cols)

print(board_string_vizualization(board_se_02))

fill_all_dot_cells(board,block_rows, block_cols)

print(board_to_string(board,rows,cols))

board_updated = elimination_technique(board, rows, cols)
print(board_to_string(board_updated, rows, cols))
