# This file has the implementation for all the functions that compose the Elimination Technique

# Helper function - Make a string with the missing elements of a block
def missing_elements(board, selected_rows, selected_cols):
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
			board[position] = missing_elements(board, selected_rows, selected_cols)

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

