from tictactoe import *

test_board=[['X', 'O', 'X'],
            ['O', 'O', 'X'],
            [EMPTY, EMPTY, EMPTY]]

test_board2=[['X', 'O', 'X'],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

test_board3=[['O', 'X', 'X'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X']]


#initial_board=initial_state()


#print (f'the turn is {player(test_board)}')
#print (max_value_alpha_beta(test_board,-2,2))
#print (min_value_alpha_beta(test_board,-2,2))

#print (terminal(test_board3))
#print (utility(test_board3))

#minimax(test_board)
#minimax(test_board2)
#minimax(initial_board)

print (winner(test_board3))