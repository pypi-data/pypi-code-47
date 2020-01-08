# --------------------------------------------------------------------
# jokettt project, v. 0.1
# by F. Piantini <francesco.piantini@gmail.com>
# ---
# Tic Tac Toe perfect minimax Player class definition
#
# --- Credits:
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-2-evaluation-function/
#
# ---
# Minimax algo applied to TicTacToe game
#  - with alpha-beta-pruning
#  - with (Zobrist) hash evaluation function
# --------------------------------------------------------------------

"""Implementation of the Minimax Player:
    a tic-tac-toe perfect minimax Player with alpha-beta-pruning
    This class is derived from the Player base class
    This player has a "dumb" mode that can be activated at any step:
    in this mode, a random move is chosen
"""
from copy import deepcopy

from random import randint
from random import shuffle

from jokettt.board.board import Board
from jokettt.players.player import Player

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods
class MinimaxParameters:
    """Parameters for a minimax algorithm with alpha-beta pruning."""
    def __init__(self, depth=0, is_maximizer=True, alpha=-1000, beta=1000):
        self.depth = depth
        self.is_maximizer = is_maximizer
        self.alpha = alpha
        self.beta = beta
# pylint: enable=too-few-public-methods

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class MinimaxPlayer(Player):
    """A Tic Tac Toe minimax automatic player."""

    # ----------------------------------------------------------------------------------------
    def __init__(self, piece, dumb_mode=False, verbosity=0):
        """MinimaxPlayer class constructor. Save the given piece,
            and enable dumb mode is requested."""
        Player.__init__(self, piece, verbosity)
        self.set_dumb_mode(dumb_mode)

    # ----------------------------------------------------------------------------------------
    def set_dumb_mode(self, dumb_mode):
        """Enable or disable the dumb mode"""
        self.__dumb_mode = dumb_mode

    # ----------------------------------------------------------------------------------------
    def move(self, board):
        """Do a move using currently selected mode (dumb or minimax)"""
        if self.__dumb_mode:
            return self.__move_dumb(board)
        return self.__move_smart(board)

    # ----------------------------------------------------------------------------------------
    def __move_smart(self, board):
        """Do a smart move (using minimax algo). If this is the first move,
            performs a random move using dumb mode"""
        if board.is_empty():
            ###print("I'm smart, but this is first move... choose random move")
            return self.__move_dumb(board)

        ###print("I'm smart, choose best move")
        _, best_x, best_y = self.__find_move_minimax(board, MinimaxParameters(0, True, -1000, 1000))
        return best_x, best_y

    # ----------------------------------------------------------------------------------------
    def __find_move_minimax(self, board, mm_par):
        """Find the best move (or one of the best) using the minimax algo"""
        best_x = None
        best_y = None
        val = board.evaluate(self.piece)
        if val != 0 or board.is_full():
            # evaluate function returns a positive value
            # if maximizer win, a negative value otherwise
            if val > 0:
                return val - mm_par.depth, best_x, best_y
            return val + mm_par.depth, best_x, best_y

        move_list = board.valid_moves()
        shuffle(move_list)  # to add some variability to the play (...maybe)
        if mm_par.is_maximizer:
            best_score = -1000
            for move in move_list:
                simul_board = deepcopy(board)
                simul_board.place_pawn(move[0], move[1], self.piece)
                score, _, _ = self.__find_move_minimax(simul_board, \
                       MinimaxParameters(mm_par.depth+1, False, mm_par.alpha, mm_par.beta))
                if score > best_score:
                    best_score = score
                    best_x = move[0]
                    best_y = move[1]
                mm_par.alpha = max(mm_par.alpha, best_score)
                if mm_par.beta <= mm_par.alpha:
                    break
        else:
            best_score = 1000
            for move in move_list:
                simul_board = deepcopy(board)
                simul_board.place_pawn(move[0], move[1], self.other_piece)
                score, _, _ = self.__find_move_minimax(simul_board, \
                       MinimaxParameters(mm_par.depth+1, True, mm_par.alpha, mm_par.beta))
                if score < best_score:
                    best_score = score
                    best_x = move[0]
                    best_y = move[1]
                mm_par.beta = min(mm_par.beta, best_score)
                if mm_par.beta <= mm_par.alpha:
                    break

        return best_score, best_x, best_y

    # ----------------------------------------------------------------------------------------
    @staticmethod
    def __move_dumb(board):
        """Do a dumb move"""
        ###print("I'm dumb, choose random move")
        if board.is_full():
            return None, None
        while True:
            _x = randint(0, 2)
            _y = randint(0, 2)
            if board.pos_is_empty(_x, _y):
                return _x, _y
