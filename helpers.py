#This file contains the helpers functions that all the others files use

#  ================================ >> Preparation Functions << =================================

# Helper function - creates dictionary from string representation
def create_dict_representation(board, rows, cols):
    possible_comb = [r+c for r in rows for c in cols]
    map_board = {p:b for b, p in zip(board, possible_comb)}
    return map_board

# Helper function - fills all the cells that are with dot for the possibles elements left in the block
def fill_all_dot_cells(board, rows, cols, elements_string):
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if board[position] == '.':
			board[position] = elements_string

#  ======================= >> Board Visualizaiton Functions (strings) << ========================

# Helper function - creates visualization from the inicial string to the string representation with rows and columns
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

# Creates a string representation for a 9x9 grid, from a MAP to a STRING with rows and columns for the board
def board_to_string_9x9(board, rows, cols):
	string = '------|-------|-------\n'
	positions = [r+c for r in rows for c in cols]
	count = 0
	count2 = 0
	for position in positions:
		count += 1
		if (count % 3 != 0):
			string += board[position] + ' '
		else:
			string += board[position] + " | "
		if (count == 9) :
			string += '\n'
			count = 0
			count2 += 1
			if (count2 % 3 == 0):
				string += '------|-------|-------\n'
		
	return string

# Creates a string representation for a 16x16 grid, from a MAP to a STRING with rows and columns for the board
def board_to_string_16x16(board, rows, cols):
	string = '--------|--------|--------|--------\n'
	positions = [r+c for r in rows for c in cols]
	count = 0
	count2 = 0
	for position in positions:
		count += 1
		if (count % 4 != 0):
			string += board[position] + ' '
		else:
			string += board[position] + " | "
		if (count == 16) :
			string += '\n'
			count = 0
			count2 += 1
			if (count2 % 4 == 0):
				string += '--------|--------|--------|--------\n'
		
	return string

# Print the string of a board using the function maded for the choosed grid
def print_board(board, rows, cols, grid):
		if(grid == 9):
			print(board_to_string_9x9(board, rows, cols))
		else:
			print(board_to_string_16x16(board, rows, cols))

#  ============================= >> Technical Helpers Functions << ==============================

#Helper Function - Returns True if the index element is unique in the string
def is_unique(elements_string, element_index):
	
	element_search = elements_string[element_index]
	for i in range(len(elements_string)):
		if i != element_index:
			if elements_string[i] == element_search:
				return False

	return True

def is_unique_block(board, selected_rows, selected_cols):
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		string += board[position]

	i = 0
	while i < len(string):
		if (is_unique(string, i)):
			i += 1
		else:
			return False

	return True


# Helper function - Returns an boolean value, True if all positions have only one value alocated and False otherwise
def check_solution(board, rows, cols, block_rows, block_cols):
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if (len(board[position]) > 1):
			return False
	return True 