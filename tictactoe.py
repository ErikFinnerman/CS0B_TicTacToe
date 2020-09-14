"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():  # X starts in initial state
        return 'X'
    else:
        turn = 0
        for row in board:
            for j in row:
                if j == 'X':
                    turn = turn + 1
                elif j == 'O':
                    turn = turn - 1
        if turn == 1:
            return 'O'
        else:
            return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()  # creating the action set
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell == EMPTY:
                actions.add((i, j))
            j = j + 1
        i = i + 1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        if action not in actions(board):
            raise ValueError
        new_board = copy.deepcopy(board)
        turn = player(board)  # returns 'X' or 'O'
        new_board[action[0]][action[1]] = turn
        return new_board
    except ValueError as e:
        print('Action not compatible with board!')
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check each row
    for row in board:
        if row.count('X') == 3 or row.count('O') == 3:
            return row[0]
    # check each column
    for col_no in [0,1,2]:
        count = 0
        j = 0
        col = (board[0][col_no], board[1][col_no], board[2][col_no])
        if col.count('X') == 3 or col.count('O') == 3:
            return col[0]
    # Check each diagonal
    d1 = [board[0][0], board[1][1], board[2][2]]
    if d1.count('X') == 3:
        return 'X'
    elif d1.count('O') == 3:
        return 'O'
    d2 = [board[0][2], board[1][1], board[2][0]]
    if d2.count('X') == 3:
        return 'X'
    elif d2.count('O') == 3:
        return 'O'
    return None  # No winner identified after all checks


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if winner
    if winner(board) in ('X', 'O'):
        return True

    # If no winner, check if board is filled
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False  # I.e. there is at least one more cell to fill
    return True  # Assume terminal state if board was filled but no winner


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def max_value_alpha_beta(board, alpha, beta):
    """ Returns max value of possible moves, and best move (i,j)"""
    if terminal(board):
        return [utility(board), None, None]
    v = float("-inf")
    for action in actions(board):
        v0 = v
        v = max(v, min_value_alpha_beta(result(board, action),alpha,beta)[0])
        if not v == v0:
            max_action = action #Will adjust the max_action at least once
        if v >= beta:
            max_action = action
            return [v, max_action]
        if v>alpha:
            alpha=v
    return [v, max_action]


def min_value_alpha_beta(board,alpha,beta):
    """ Returns min value of possible moves, and best move (i,j)"""

    if terminal(board):
        return [utility(board), (None, None)]  # No action specified since terminal value
    v = float("inf")
    for action in actions(board):
        v0 = v
        v = min(v, max_value_alpha_beta(result(board, action),alpha,beta)[0])
        if not v == v0:
            min_action = action
        if v<=alpha:
            min_action = action
            return [v,min_action]
        if v<beta:
            beta=v
    return [v, min_action]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == 'X':  # Want to maximize utility
        best_action = max_value_alpha_beta(board,-2,2)
    else:
        best_action = min_value_alpha_beta(board,-2,2)

    return best_action[1]
