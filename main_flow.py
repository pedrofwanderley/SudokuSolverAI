import grids
import helpers
import elimination
import only_choice
import heuristic
import samurai
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

def resolution_samurai(boards_list, nivel):
	#Grid's coordinates for 9x9 boards
	rows = 'ABCDEFGHI'
	cols = rows
	block_rows = ['ABC', 'DEF', 'GHI']
	block_cols = block_rows
	elements_string = '123456789'
	grid = 9

	boards_maps = []
	for board in boards_list: 
		board = prepare_board(board, rows, cols, elements_string, grid)
		boards_maps.append(board)
	if(nivel == 1):
		flag = samurai.super_easy_solution_flow(boards_maps, rows, cols, block_rows, block_cols, grid)
	if(nivel == 2):
		flag = samurai.general_solution_flow(boards_maps, rows, cols, block_rows, block_cols, grid)
	if flag:
		print('=====>> The Grid Was Solved With Sucess <<=====\n')
	else:
		print('=====>> The Time To Find a Solution is Over <<=====\n')

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

def menu_apresentacao():
	while True:
		print("============= >> Welcome to the Sudoku Solver << ============")
		print("======== >> Select a GRID to see a resolution flow << =======")
		print("(1) 9x9")
		print("(2) 16x16")
		print("(3) Samurai")
		print("(4) Sair")
		entrada = int(input("Insert your GRID TYPE input: "))
		if(entrada == 4):
			print("======== >> Bye Bye ✌  << =======")
			break
		if(entrada == 1):
			menu_9x9()
		if(entrada == 2):
			menu_16x16()
		if(entrada == 3):
			menu_samurai()


def menu_9x9():
	while True:
		print("======= >> You choosed to see a 9x9 resolution flow << ======")
		print("(1) Super Easy")
		print("(2) Easy")
		print("(3) Medium")
		print("(4) Hard")
		print("(5) Get Back to Home")
		entrada = int(input("Insert your GRID TYPE input: "))
		if(entrada == 5):
			break
		if(entrada == 1): resolution_9x9(grids.board_se_01_9x9)
		if(entrada == 2): resolution_9x9(grids.board_e_01_9x9)
		if(entrada == 3): resolution_9x9(grids.board_m_01_9x9)
		if(entrada == 4): resolution_9x9(grids.board_h_02_9x9)

def menu_16x16():
	while True:
		print("======= >> You choosed to see a 16x16 resolution flow << ======")
		print("(1) Easy")
		print("(2) Medium")
		print("(3) Get Back to Home")
		entrada = int(input("Insert your GRID TYPE input: "))
		if(entrada == 3):
			break
		if(entrada == 1): resolution_16x16(grids.board_e_01_16x16)
		if(entrada == 2): resolution_16x16(grids.board_m_01_16x16)

def menu_samurai():
	while True:
		print("======= >> You choosed to see a ⊰⋋SAMURAI⋌⊱ resolution flow << ======")
		print("(1) Easy")
		print("(2) Medium")
		print("(3) Get Back to Home")
		entrada = int(input("Insert your GRID TYPE input: "))
		if(entrada == 3):
			break
		if(entrada == 1): resolution_samurai(grids.board_se_01_samurai, entrada)
		if(entrada == 2): resolution_samurai(grids.board_m_01_samurai, entrada)


menu_apresentacao()



