import helpers
import elimination
import only_choice
import grids
import time

def prepare_board(boards_string, rows, cols, elements_string):
	board = helpers.create_dict_representation(boards_string, rows, cols)
	helpers.fill_all_dot_cells(board,rows, cols, elements_string)

	return board

def general_solution_flow(board, rows, cols, block_rows, block_cols):
	count = 0
	while (helpers.check_solution(board, rows, cols, block_rows, block_cols) == False and count < 100):
		board = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
		print(helpers.board_to_string(board, rows, cols))
		if (helpers.check_solution(board, rows, cols, block_rows, block_cols)):
			return True

		board = only_choice.all_only_choices(board, block_rows, block_cols)
		print(helpers.board_to_string(board, rows, cols))
		if (helpers.check_solution(board, rows, cols, block_rows, block_cols)):
			return True

		count += 1

	return False
			


def resolution_9x9(boards_string):
	#Grid's coordinates for 9x9 boards
	rows = 'ABCDEFGHI'
	cols = rows
	block_rows = ['ABC', 'DEF', 'GHI']
	block_cols = block_rows
	elements_string = '123456789'

	board = prepare_board(boards_string, rows, cols, elements_string)

	flag = general_solution_flow(board, rows, cols, block_rows, block_cols)
	if (flag) :
		print('=====>> The Grid Was Solved With Sucess <<=====\n')
	else:
		print('=====>> The Time To Find a Solution is Over <<=====\n')
	
	return helpers.check_solution(board, rows, cols, block_rows, block_cols)


def resolution_16x16(boards_string):
	#Grid's coordinates for 9x9 boards
	rows = 'ABCDEFGHIJKLMNOP'
	cols = rows
	block_rows = ['ABCD', 'EFGH', 'IJKL', 'MNOP']
	block_cols = block_rows
	elements_string = '123456789ABCDEFG'
	
	board = prepare_board(boards_string, rows, cols, elements_string)
	
	flag = general_solution_flow(board, rows, cols, block_rows, block_cols)
	if (flag) :
		print('=====>> The Grid Was Solved With Sucess <<=====\n')
	else:
		print('=====>> The Time To Find a Solution is Over <<=====\n')
	
	return helpers.check_solution(board, rows, cols, block_rows, block_cols)




def compareSolutionsTimes(func1, func2):

	ini_func1 = time.time()
	func1(1, 1000000)
	fim_func1 = time.time()
	print("Função 1: ", fim_func1-ini_func1)

	# verifica o tempo de resposta da função soma2
	ini_func2 = time.time()
	func2(1, 1000000)
	fim_func2 = time.time()
	print("Função 2: ", fim_func2-ini_func2)


resolution_9x9(grids.board_se_01_9x9)
resolution_9x9(grids.board_e_01_9x9)
resolution_9x9(grids.board_m_01_9x9)
#resolution_16x16(grids.board_m_01_16x16)

