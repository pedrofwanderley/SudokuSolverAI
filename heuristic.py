#String representation
#Super Easy Boards
#se = super easy

board_se_01 = '67...15.92...9..149.1.3.2.7..7..48...62.7839.58.2..476.2..4.165.56.8.943.943...28'
board_se_02 = '12.935..8.8627.5..935.461.77.1.6.28.358.......6.518.7987.6.2..1..91..7..512.9..36'
board_se_03 = '23...176.....8.43.1.65...9.3276.9.8.581.3..2..9.1283..9.2317.4....86527....942613'
board_se_04 = '..49....6.96..427.2831....4......7253.72.984142...5.93..9521..77.569318.6..84.53.'

board_se_05 = '12.93.4684.62.1593935.461277.13.428.358.29614.6451.379873.5294.64.183.52..2.97836'

rows = 'ABCDEFGHI'
cols = '123456789'
block_rows = ['ABC', 'DEF', 'GHI']
block_cols = ['123', '456', '789']
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []

def populateList(board, rows, cols):
	positions = [r+c for r in rows for c in cols]
	for position in positions:
	        populateLists(position,board)


def populateLists(element,board):
	if(element[0] == "A" and board[element] != "." and len(board[element]) == 1):
		a.append(board[element])

# Helper function - creates dictionary from string representation
def create_dict_representation(board, rows, cols):
    possible_comb = [r+c for r in rows for c in cols]
    map_board = {p:b for b, p in zip(board, possible_comb)}
    return map_board

#The board used to delevolp the code as test (board_se_02)
dict_board = create_dict_representation(board_se_02, rows, cols)
board = dict_board

# Helper function - Make a string with the missing elements of a block
def missing_elements(selected_rows, selected_cols):
	missing_elements = '123456789'
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		if (board[position] in '123456789' or board[position] in a):
			missing_elements = missing_elements.replace(board[position], '')

	return missing_elements

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

# Helper function - fills the cells of a block that are with a dot for the possibles elements left
def fill_block_dot_cells(board, selected_rows, selected_cols):
	positions = [r+c for r in selected_rows for c in selected_cols]
	for position in positions:
		if board[position] == '.':
			missing = missing_elements(selected_rows, selected_cols);
			for elemento in missing:
				if(elemento in verificaLinhaColuna(position, board, rows, cols) and len(missing) > 1):
					missing = missing.replace(elemento, '')
			if(missing != "" and len(missing) == 1):
				board[position] = missing
			else:
				board[position] = missing_elements(selected_rows, selected_cols)


# Helper function - fills all the cells that are with dot for the possibles elements left in the block
def fill_all_dot_cells(board, block_rows, block_cols):
	for r in block_rows:
		for c in block_cols:
			fill_block_dot_cells(board,r,c)

fill_all_dot_cells(board,block_rows, block_cols)
#print(board)
#print('\n\n\n')

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
	valuesof = sortList(empty_positions_list)

	for position in valuesof:
		row_missing = position[0]
		missing_elements = board[position]
		allocated_elements_row = row_to_string(board, row_missing, cols)
		board[position] = eliminate_peer_in_a_string(missing_elements, allocated_elements_row)


	updated_empty_positions_list = empty_positions(board, rows, cols)
	valuesof2 = sortList(updated_empty_positions_list)
	#Eliminates possibles elements by columns
	for position in valuesof2:
		col_missing = position[1]
		missing_elements = board[position]
		allocated_elements_col = col_to_string(board, col_missing, rows)
		board[position] = eliminate_peer_in_a_string(missing_elements, allocated_elements_col)

	return board

# Makes a loop to eliminate all the redundant elements in the grid
def elimination_technique(board, rows, cols):
	valuesof = []
	empty_positions_list = empty_positions(board,rows, cols)
	valuesof = sortList(empty_positions_list)
	while(len(valuesof) > 0):
		print(board_to_string(board,rows,cols))
		board_updated = eliminate_peer(board,rows,cols,valuesof)
		empty_positions_list = empty_positions(board_updated,rows, cols)
		valuesof = sortList(empty_positions_list)


	return board_updated

def sortList(lista):
	values = []
	valuesof = []
	empty_positions_list = empty_positions(board,rows, cols)
	for p in empty_positions_list:
		values.append(p + " " + board[p])
		values.sort(key=lambda x:int(x.split()[-1]))
	for v in values:
		valuesof.append(v[0:2])
	return valuesof
# To see the final elimination technique result for the board_se_02
print(board_to_string(board,rows,cols))
board_updated = elimination_technique(board, rows, cols)
print(board_to_string(board_updated, rows, cols))
