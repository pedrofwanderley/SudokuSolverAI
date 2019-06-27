# This file has the implementation for all the functions that compose the Elimination Technique

import helpers

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
	valuesof = []
	valuesof2 = []
	valuesof = sortList(rows, cols, board, empty_positions_list)

	for position in valuesof:
		row_missing = position[0]
		missing_elements = board[position]
		allocated_elements_row = row_to_string(board, row_missing, cols)
		board[position] = eliminate_peer_in_a_string(missing_elements, allocated_elements_row)


	updated_empty_positions_list = empty_positions(board, rows, cols)
	valuesof2 = sortList(rows, cols, board, updated_empty_positions_list)
	#Eliminates possibles elements by columns
	for position in valuesof2:
		col_missing = position[1]
		missing_elements = board[position]
		allocated_elements_col = col_to_string(board, col_missing, rows)
		board[position] = eliminate_peer_in_a_string(missing_elements, allocated_elements_col)

	return board

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

def sortList(rows, cols, board, lista):
	values = []
	valuesof = []
	empty_positions_list = empty_positions(board,rows, cols)
	for p in empty_positions_list:
		values.append(p + " " + board[p])
		values.sort(key=lambda x:int(x.split()[-1]))
	for v in values:
		valuesof.append(v[0:2])
	return valuesof


def verificaLinhaColuna(posicao, board, rows, cols):
	values = []
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if((position[0] == posicao[0] or position[1] == posicao[1]) and len(board[position]) == 1 and board[position] != "."):
			values.append(board[position])

	return values

def verificaLinha(posicao, board, rows, cols):
	valuesLinhas = []
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if((position[0] == posicao[0]) and len(board[position]) == 1 and board[position] != "."):
			valuesLinhas.append(board[position])


	return valuesLinhas

def verificaColuna(posicao, board, rows, cols):
	valuesColunas = []
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if((position[1] == posicao[1]) and len(board[position]) == 1 and board[position] != "."):
			valuesColunas.append(board[position])


	return valuesColunas

def menosPossibilidades(board, rows, cols):
	menor = 999999
	positions = [r+c for r in rows for c in cols]
	for position in positions:
		if(len(board[position]) < menor and len(board[position]) > 1):
			menor = board[position]


	return menor

# Makes a loop to eliminate all the redundant elements in the grid
def heuristic_technique(board, rows, cols, block_rows, block_cols):
	heuristic_values = []
	empty_positions_list = empty_positions(board,rows, cols)
	heuristic_values = sortList(rows, cols, board, empty_positions_list)
	count = 0
	#while(helpers.check_solution(board, rows, cols) == False):
	while(len(heuristic_values) > 0):
		if count > 20 :
			break
		else:
			board_updated = eliminate_peer(board,rows,cols,heuristic_values)
			update_all_missing_elements(board_updated, block_rows, block_cols)
			empty_positions_list = empty_positions(board_updated,rows, cols)
			heuristic_values = sortList(rows, cols, board, empty_positions_list)
			count += 1

	print('=====>> After Heuristic Technique <<=====\n')
	return board_updated