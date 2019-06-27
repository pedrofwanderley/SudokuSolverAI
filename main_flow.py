import grids
import helpers
import elimination
import only_choice
import heuristic
import time

def prepare_board(boards_string, rows, cols, elements_string, grid):
	board = helpers.create_dict_representation(boards_string, rows, cols)
	helpers.fill_all_dot_cells(board,rows, cols, elements_string)
	print('=====>> Board With all The Possibilities <<=====\n')
	helpers.print_board(board, rows, cols, grid)
	return board

# Fluxo genérico para resolução dos grids, iniciando pela eliminação seguida da only_choice. 
# A heuristica é chamanda apenas quando as primeiras técnica não encontram uma solução.
def general_solution_flow(board, rows, cols, block_rows, block_cols, grid):
	count_general_loops = 0
	count_to_heuristic_loops = 0
	while (helpers.check_solution(board, rows, cols, block_rows, block_cols) == False and count_general_loops < 100):
		board = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
		helpers.print_board(board, rows, cols, grid)
		if (helpers.check_solution(board, rows, cols, block_rows, block_cols)):
			return True

		board = only_choice.all_only_choices(board, block_rows, block_cols)
		helpers.print_board(board, rows, cols, grid)
		if (helpers.check_solution(board, rows, cols, block_rows, block_cols)):
			return True

		count_to_heuristic_loops += 1
		if(count_to_heuristic_loops > 10):
			board = heuristic.heuristic_technique(board, rows, cols, block_rows, block_cols)
			helpers.print_board(board, rows, cols, grid)
			if (helpers.check_solution(board, rows, cols, block_rows, block_cols)):
				return True

		count_general_loops += 1

	return False
			


def resolution_9x9(boards_string):
	#Grid's coordinates for 9x9 boards
	rows = 'ABCDEFGHI'
	cols = rows
	block_rows = ['ABC', 'DEF', 'GHI']
	block_cols = block_rows
	elements_string = '123456789'

	board = prepare_board(boards_string, rows, cols, elements_string, 9)

	flag = general_solution_flow(board, rows, cols, block_rows, block_cols, 9)
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
	
	board = prepare_board(boards_string, rows, cols, elements_string, 16)
	
	flag = general_solution_flow(board, rows, cols, block_rows, block_cols,16)
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

# ===== >> Grids 9x9 << =====
#resolution_9x9(grids.board_se_01_9x9)
#resolution_9x9(grids.board_e_01_9x9)
#resolution_9x9(grids.board_m_01_9x9)
#resolution_9x9(grids.board_h_02_9x9)

# ===== >> Grids 16x16 << =====
#resolution_16x16(grids.board_m_01_16x16)

# ===== >> Grids Samurai << =====
#resolution_9x9(grids.board_01_samurai)



