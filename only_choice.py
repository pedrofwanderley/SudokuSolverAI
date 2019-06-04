# Helper function - Make a string with the already allocated elements of a block
def allocated_elements(board, selected_rows, selected_cols):
	allocated_elements = ''
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		if(len(board[position]) == 1):
			allocated_elements += board[position]

	return allocated_elements	


# Helper function - update the positions with more than one value with the new allocated elements
def update_missing_elements_block(board, selected_rows, selected_cols):
	block_elements = allocated_elements(board, selected_rows, selected_cols)
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		if (len(board[position]) > 1):
			for element in board[position]:
				if (element in block_elements):
					board[position] = board[position].replace(element, '')

# Helper function - update all grid positions with more than one value after the elimination technique
def update_all_missing_elements(board, block_rows, block_cols):
	for r in block_rows:
		for c in block_cols:
			update_missing_elements_block(board,r,c)

#Helper Function - Returns True if the index element is unique in the string
def is_unique(elements_string, element_index):
	
	element_search = elements_string[element_index]
	for i in range(len(elements_string)):
		if i != element_index:
			if elements_string[i] == element_search:
				return False

	return True

# Update positions with the only choice possible in a given block
def find_only_choice_block(board, selected_rows, selected_cols):
	positions = [r+c for r in selected_rows for c in selected_cols]
	elements_left = ''
	elements_left_posicion = []
	for position in positions:
		if (len(board[position]) > 1):
			elements_left += board[position]
			for element in board[position]:
				elements_left_posicion.append(position)

	for i in range(len(elements_left)):
		if(is_unique(elements_left, i)):
			board[elements_left_posicion[i]] = elements_left[i]

			
# Eliminates a possible element position that is already in a row or column
def all_only_choices(board, block_rows, block_cols):
	for r in block_rows:
		for c in block_cols:
			find_only_choice_block(board,r,c)

	return board
