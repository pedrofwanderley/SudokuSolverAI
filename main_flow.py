import elimination
import only_choice
import grids
import time

# Gri's coordinates
rows = 'ABCDEFGHI'
cols = '123456789'
block_rows = ['ABC', 'DEF', 'GHI']
block_cols = ['123', '456', '789']
elements_string = '123456789'

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
	string = '------|-------|--------\n'
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
				string += "------|-------|--------\n"
	return string


def level_resolution(boards_list, level):
	for b in boards_list:
		print(board_string_vizualization(b))
		board = create_dict_representation(b, rows, cols)
		elimination.fill_all_dot_cells(board,rows, cols, elements_string)
		print(board_to_string(board,rows,cols))

		if (level == 'SE'):
			board_updated = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
			print(board_to_string(board_updated, rows, cols))
		if (level == 'E'):
			board_updated = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
			print(board_to_string(board_updated, rows, cols))
		if (level == 'M'):
			board_updated = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
			print(board_to_string(board_updated, rows, cols))
		print('\n>> ---------------------------------- << \n')

# def only_choice_test(b):
# 	print(board_string_vizualization(b))
# 	board = create_dict_representation(b, rows, cols)
# 	elimination.fill_all_dot_cells(board, block_rows, block_cols)
# 	print(board_to_string(board,rows,cols))

# 	count = 0
# 	empty_positions_list = elimination.empty_positions(board,rows, cols)
# 	while(count <= 20):
# 		board_updated = elimination.eliminate_peer(board,rows,cols,empty_positions_list)
# 		empty_positions_list = elimination.empty_positions(board_updated,rows, cols)
# 		count += 1

# 	print(board_to_string(board_updated,rows,cols))
# 	print(check_solution(board_updated, rows, cols))

# 	if(check_solution(board_updated, rows, cols) == False):
# 		count = 0
# 		while(count <= 2):
# 			only_choice.update_all_missing_elements(board, block_rows, block_cols)
# 			count += 1
# 	print(check_solution(board_updated, rows, cols))

# 	if(check_solution(board_updated, rows, cols) == False):
# 		count = 0
# 		empty_positions_list = elimination.empty_positions(board,rows, cols)
# 		while(count <= 20):
# 			board_updated = elimination.eliminate_peer(board,rows,cols,empty_positions_list)
# 			empty_positions_list = elimination.empty_positions(board_updated,rows, cols)
# 			count += 1

# 	print(board_to_string(board_updated,rows,cols))

# 	print('\n>> ---------------------------------- << \n')

# Helper function - Returns an boolean value, True if all positions have only one value alocated and False otherwise
def check_solution(board, rows, cols):
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if (len(board[position]) > 1):
			return False


	return True

def compareSolutionsTimes(func1, func2):

	ini_func1 = time.time()
	func1(1, 1000000)
	fim_func1 = time.time()
	print "Função 1: ", fim_func1-ini_func1

	# verifica o tempo de resposta da função soma2
	ini_func2 = time.time()
	func2(1, 1000000)
	fim_func2 = time.time()
	print "Função 2: ", fim_func2-ini_func2


#To see the elimination technique flow with the Super Easy Boards
level_resolution(grids.super_easy_boards, 'SE')
level_resolution(grids.easy_boards, 'E')
level_resolution(grids.medium_boards, 'M')

#only_choice_test(grids.board_e_05)
