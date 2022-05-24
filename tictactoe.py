
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
    xcount = 0
    ocount = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount +=1
    if xcount > ocount:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possible_action.add((i, j))
    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][1] == board[0][2] == board[0][0]!=None:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]!=None:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]!=None:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]!=None:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]!=None:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]!=None:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]!=None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]!=None:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    fullboard = 0
    for i in range(0, len(board)):
     for j in range(0, len(board[0])):
        if board[i][j] != EMPTY:
            fullboard += 1

    if winner(board) is not None or (winner(board) is None and fullboard == 9):
       return True
    else:
       return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
            return 1
    elif winner(board) == O:
            return -1
    else:
            return 0



def minimax(board):
    if terminal(board):
        return None
    allowable_actions = list(actions(board))
    if player(board) == X:
        values = [min_value(result(board, action)) for action in allowable_actions]
        v = max(values)
    else:
        values = [max_value(result(board, action)) for action in allowable_actions]
        v = min(values)
    first = values.index(v)
    optimal_action = allowable_actions[first]
    return optimal_action



def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
         return utility(board)
    v = float('inf')
    for action in actions(board):
       v = min(v,max_value(result(board, action)))
    return v

