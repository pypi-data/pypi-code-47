# --------------------------------------------------------------------
# jokettt project, v. 0.1
# by F. Piantini <francesco.piantini@gmail.com>
# ---
# Tic Tac Toe Player base class definition
# --------------------------------------------------------------------
# pylint: disable=too-few-public-methods

"""Implementation of the Player base abstract class:
    a generic player that has a piece and it is able to perform a move.
    This class shall not be used directly: it shall be used as a base
    class for real players
"""
from abc import ABC, abstractmethod

class Player(ABC):
    """A Tic Tac Toe player base class."""
    def __init__(self, piece, verbosity=0):
        """Player class constructor."""
        self.piece = piece
        self.__verbosity = verbosity
        if piece == "x":
            self.other_piece = "o"
        else:
            self.other_piece = "x"

        ABC.__init__(self)

    @abstractmethod
    def move(self, board):
        """Method to make a move. This is the base player,
            so this method is abstract."""

    def log_info(self, *args):
        """print a log line if verbosity > 0"""
        if self.__verbosity > 0:
            print(*args)
