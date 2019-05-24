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
