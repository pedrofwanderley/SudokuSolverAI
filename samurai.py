import grids
import helpers
import elimination
import only_choice
import heuristic

# Merges all the possibiliteis from one intersection of two boards, where
# board_n and board_m: boards whose the blocks in common will be merged
# n_cols and n_rows: the selected cols and rows from board_n
# m_cols and m_rows: the selected cols and rows from board_m
def merge_intersection(board_n, board_m, n_cols, n_rows, m_cols, m_rows):
	positions_n = [r+c for r in n_rows for c in n_cols]
	positions_m = [y+x for y in m_rows for x in m_cols]
	
	elements_string = ''

	for i in range(9):
		elements_string = ''
		for element in board_m[positions_m[i]]:
			if (element in board_n[positions_n[i]]):
				elements_string += element
		board_n[positions_n[i]] = elements_string
		board_m[positions_m[i]] = elements_string


def all_merge_intersection(board_1, board_2, board_3, board_4, board_5):
	merge_intersection(board_1, board_3,  'GHI', 'GHI', 'ABC', 'ABC')
	merge_intersection(board_2, board_3,  'ABC', 'GHI', 'GHI', 'ABC')
	merge_intersection(board_4, board_3,  'GHI', 'ABC', 'ABC', 'GHI')
	merge_intersection(board_5, board_3,  'ABC', 'ABC', 'GHI', 'GHI')

def general_solution_flow(boards_list, rows, cols, block_rows, block_cols, grid):
	count = 0
	while(count < 4):
		for board in boards_list:
			board = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
			helpers.print_board(board, rows, cols, grid)
			board = only_choice.all_only_choices(board, block_rows, block_cols)
			helpers.print_board(board, rows, cols, grid)
			board = heuristic.heuristic_technique(board, rows, cols, block_rows, block_cols)
			helpers.print_board(board, rows, cols, grid)
		
		all_merge_intersection(boards_list[0], boards_list[1], boards_list[2], boards_list[3], boards_list[4])
		
		count += 1
	
	check_board_1 = helpers.check_solution(boards_list[0], rows, cols, block_rows, block_cols)
	check_board_2 = helpers.check_solution(boards_list[1], rows, cols, block_rows, block_cols)
	check_board_3 = helpers.check_solution(boards_list[2], rows, cols, block_rows, block_cols)
	check_board_4 = helpers.check_solution(boards_list[3], rows, cols, block_rows, block_cols)
	check_board_5 = helpers.check_solution(boards_list[4], rows, cols, block_rows, block_cols)
	
	return (check_board_1, check_board_2, check_board_3, check_board_4, check_board_5)

def super_easy_solution_flow(boards_list, rows, cols, block_rows, block_cols, grid):
	for board in boards_list:
		board = elimination.elimination_technique(board, rows, cols, block_rows, block_cols)
		helpers.print_board(board, rows, cols, grid)
	all_merge_intersection(boards_list[0], boards_list[1], boards_list[2], boards_list[3], boards_list[4])
	
	check_board_1 = helpers.check_solution(boards_list[0], rows, cols, block_rows, block_cols)
	check_board_2 = helpers.check_solution(boards_list[1], rows, cols, block_rows, block_cols)
	check_board_3 = helpers.check_solution(boards_list[2], rows, cols, block_rows, block_cols)
	check_board_4 = helpers.check_solution(boards_list[3], rows, cols, block_rows, block_cols)
	check_board_5 = helpers.check_solution(boards_list[4], rows, cols, block_rows, block_cols)
	
	return (check_board_1, check_board_2, check_board_3, check_board_4, check_board_5)


		