# ----->> String representation <<-----

#  ===== >> 9x9 Boards << ======
#Fonte: https://www.geniol.com.br/logica/sudoku/

#Super Easy Boards
#se = super easy
board_se_01_9x9 = '67...15.92...9..149.1.3.2.7..7..48...62.7839.58.2..476.2..4.165.56.8.943.943...28'
board_se_02_9x9 = '.2.935..8.8627.5..935.461.77.1.6.28.358.......6.518.7987.6.2..1..91..7..512.9..36'
board_se_03_9x9 = '23...176.....8.43.1.65...9.3276.9.8.581.3..2..9.1283..9.2317.4....86527....942613'
board_se_04_9x9 = '..49....6.96..427.2831....4......7253.72.984142...5.93..9521..77.569318.6..84.53.'

super_easy_boards = [board_se_01_9x9, board_se_02_9x9, board_se_03_9x9, board_se_04_9x9]

#Easy Boards
#e = easy
board_e_01_9x9 = '6.9.1....3..9..4...1.....3...7...34556......9..3...126.5.....8.4..8..2..9.6.3....'
board_e_02_9x9 = '.....267.6..47....8.3..92..4.1.6..9..6.2.7.4..8..4.3.2..89..7.5....25..9.573.....'
board_e_03_9x9 = '6...92.849.834...........6.8..7.5.3.59..8..12.2.4.9..8.1...........613.573.85...1'
board_e_04_9x9 = '.1....9...921...753...9..6....716.4...89.27...6.845....3..5...765...742...4....9.'
board_e_05_9x9 = '3.41.58.2.192.645.....4....8.......64.2.3.5.1............928...5.8...1.9..64.17..'
board_e_06_9x9 = '....5439..8...2......83..2.526...9.79.......5817...2.6...18..6..4...9.......6785.'
board_e_07_9x9 = '..9..6....67....8...53.41965.3.4.8.....1.8.....8.2.4.52817.95...5....27....2..9..'
board_e_08_9x9 = '..7..324.9.4..1...6.2...38146..1.......8.5.......6..54378...4.5...1..7.2.265..9..'
board_e_09_9x9 = '784..6..1.....7..6...38...964..1.8....38.94....7.5..624...95...3..6.....5..2..618'
board_e_10_9x9 = '129.6...3........9...35...8...8.39..3.1...5.2..61.5...4...76...2........9...8.134'

easy_boards = [board_e_01_9x9, board_e_02_9x9, board_e_03_9x9, board_e_04_9x9, board_e_05_9x9, board_e_06_9x9, board_e_07_9x9, board_e_08_9x9, board_e_09_9x9, board_e_10_9x9]

#Medium Boards
board_m_01_9x9 = '..8.6.........83...957..8.2.8.6.27..7.......1..24.5.8.5.4..926...13.........2.9..'
medium_boards = [board_m_01_9x9]

#Hard Boards

board_h_01_9x9 = '...753....6.....3.5...9...4...........15.92..8.5.2.9.6.8.....6.4..8.7..9..76.23..'
board_h_02_9x9 = '..8.4.3............3.5.9.8....2.6.....9.1.4..7.6...2.99...8...24.......5.1.3.5.4.'

# Fonte: https://www.sudoku.4thewww.com/16x16-sudoku.php
#  ===== >> 16x16 Boards << ======
#A=10 B=11 C=12 D=13 E=14 F=15 G=16
board_e_01_16x16 = '.B9..GD4..E.A6F.4CF.36.B.5.1G7E21.6.F2..B9A...8..D...1..46.F..........F.8153.4B76.1..C8.9..2..3.E.4D6..3.C7A8.2.38..472.6....CG5D..G.8EA34F.C51B...62..1A.B.F3.97..C.4.F5.9E....A..8..B...1C4.DG......7.F2....C3..7..A6.18.DB.9E865..3..E..9.....G.2...E.A......'

board_m_01_16x16 = '.4..8.G.B.1..6.E3..9.F.4A7.D..C..6..2B..8...3...F......D..E..2.4...8.3..7...5.........E....A.G.D..925....8..B...C.1....G..D...3....CF....6..D.47G1D.A..3..7..9..6.....B.4..9..2A.3...G...E8..B..5B3A...8..C4...1.14..B9...DF.4.5.D.4.6......2.C.9.C.G.D...1..6.F.'

#  ===== >> Samurai Boards << ======
#Super Easy
board_se_01_samurai_1 = '7.98451328247...96513.9.4.83.716..2524537861.1865297.397..532.1.5.91.3.443.682.57'
board_se_01_samurai_2 = '8..9.5.6.9.627.85.25.81...9.28.6391446..9872...91.26.5745.2.39.1923875466834..17.'
board_se_01_samurai_3 = '2.13897453.46..192.57..268362859..17.9.1.8..61..72..39...2.15.443...5921512964.78'
board_se_01_samurai_4 = '34261....518.7243.69..3.512...12...49764831...215.7..31397562...6.248391.843.1657'
board_se_01_samurai_5 = '5.438.29.9216..438.784.91.5...54.8.9..2.986.31.9.635..24.915.8671683.95.8.52763..'
board_se_01_samurai = [board_se_01_samurai_1, board_se_01_samurai_2, board_se_01_samurai_3, board_se_01_samurai_4, board_se_01_samurai_5]


board_m_01_samurai_1 = '...385....39...8..4......2.........6....769.....1...74..4...3...8...9....6...7...'
board_m_01_samurai_2 = '......1..96.....4...3....6....4....5....8...429..3...7..5.2..8....7..9.....3.6...'
board_m_01_samurai_3 = '3...1...5.....8........4....64......2...4...6......17....9........2.....5...6...3'
board_m_01_samurai_4 = '...6.9.....7..2....9..3.5..5...9..429...8....3....1....4....8...1.....95..2......'
board_m_01_samurai_5 = '...4...7....2...9...3...1..61...9.....253....5.........9......2..5...64....685...'
board_m_01_samurai = [board_m_01_samurai_1, board_m_01_samurai_2, board_m_01_samurai_3, board_m_01_samurai_4, board_m_01_samurai_5]

