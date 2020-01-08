# --------------------------------------------------------------------
# jokettt project, v. 0.1
# by F. Piantini <francesco.piantini@gmail.com>
# ---
# Tic Tac Toe Console Player class definition
# --------------------------------------------------------------------
# pylint: disable=too-few-public-methods

"""Implementation of the Console Player:
    a player that gets the moves from console. This can be used to make
    able to play an human player using a minimal command line interface.
    The moves shall be entered using the format <row><column>, with
    <row> = A, B, C and <col> = 1, 2, 3.
    This class is derived from the Player base class
"""
from jokettt.board import Board
from jokettt.player import Player

class ConsolePlayer(Player):
    """A Tic Tac Toe console player."""
    def move(self, board):
        """Method to make a move. Just read the move from console (stdin)"""
        # read move from Console
        while True:
            move = input("Move? ")
            if board.is_valid_move(move):
                return board.convert_movestring_to_indexes(move)
            print("Invalid move. Try again.")
