# --------------------------------------------------------------------
# jokettt project, v. 0.1
# by F. Piantini <francesco.piantini@gmail.com>
# ---
# Tic Tac Toe Board class definition
# --------------------------------------------------------------------
"""Implementation of the Board class: a board to play Tic Tac Toe game."""
import sys
import random

import numpy as np

class Board:
    """A board to play Tic Tac Toe game."""
    # ------------------------------------------------------
    def __init__(self, first_piece, second_piece, init_zhash=None, init_board=None):

        """Board class constructor"""
        if init_board is not None:
            self.__board = init_board
        else:
            self.__board = [['_', '_', '_'],
                            ['_', '_', '_'],
                            ['_', '_', '_']]

        self.__first_piece = first_piece
        self.__second_piece = second_piece
        self.__init_zhash(init_zhash)

    # ------------------------------------------------------
    def reset(self, init_board=None):

        """Reset the board to the given schema (default = empty)."""
        if init_board is not None:
            for _x in range(0, 3):
                for _y in range(0, 3):
                    self.__board[_x][_y] = init_board[_x][_y]
        else:
            self.__board = [['_', '_', '_'],
                            ['_', '_', '_'],
                            ['_', '_', '_']]

        # initialize Zobrist hash value
        self.__evaluate_zhash()

    # ------------------------------------------------------
    def is_empty(self):
        """Returns True if the board is empty"""
        if self.__board == [['_', '_', '_'],
                            ['_', '_', '_'],
                            ['_', '_', '_']]:
            return True

        return False

    # ------------------------------------------------------
    def only_one_piece_present(self):
        """Returns True if only one piece present on board."""
        num_pieces = 0
        for _x in range(0, 3):
            for _y in range(0, 3):
                if self.__board[_x][_y] != "_":
                    num_pieces += 1
        if num_pieces == 1:
            return True
        return False

    # ------------------------------------------------------
    def at_least_a_corner_busy(self):
        return self.__board[0][0] != '_' or \
               self.__board[0][2] != '_' or \
               self.__board[2][0] != '_' or \
               self.__board[2][2] != '_'

    # ------------------------------------------------------
    def center_is_busy(self):
        return self.__board[1][1] != '_'

    # ------------------------------------------------------
    def is_not_full(self):
        """Returns True if the board is not full."""
        for _x in range(0, 3):
            for _y in range(0, 3):
                if self.__board[_x][_y] == "_":
                    return True
        return False

    # ------------------------------------------------------
    def is_full(self):
        """Returns True if the board is full."""
        return not self.is_not_full()

    # ------------------------------------------------------
    def pos_is_empty(self, _x, _y):
        """Returns True if the given board position does not contains a pawn."""
        return bool(self.__board[_x][_y] == "_")

    # ------------------------------------------------------
    def pos_is_busy(self, _x, _y):
        """Returns True if the given board position contains a pawn."""
        return not self.pos_is_empty(_x, _y)

    # ------------------------------------------------------
    def valid_moves(self):
        """Returns the list of the valid moves in the current board state."""
        move_list = []
        for _x in range(0, 3):
            for _y in range(0, 3):
                if self.__board[_x][_y] == "_":
                    move_list.append([_x, _y])
        return move_list

    # ------------------------------------------------------
    def is_valid_move(self, move):
        """Returns True if the move is valid in the current board state."""
        # check the format of the move
        if len(move) != 2:
            return False
        _x, _y = self.convert_movestring_to_indexes(move)
        if _x == -1 or _y == -1:
            return False
        # check if the position if free in the board
        if self.pos_is_busy(_x, _y):
            return False
        return True

    # ------------------------------------------------------
    def analyze_move(self, move, piece):
        """analize a move, returning the new board hash,
           and the score of the position"""
        zhash, score = self.place_pawn(move[0], move[1], piece)
        # return the board in the previous status
        _ = self.__remove_pawn(move[0], move[1])
        return zhash, score

    # ------------------------------------------------------
    def place_pawn(self, _x, _y, piece):
        """Places a pawn in the given board position."""
        if self.pos_is_empty(_x, _y):
            self.__board[_x][_y] = piece
            self.__update_zhash(_x, _y, piece)
        return self.evaluate(piece)

    # ------------------------------------------------------
    def evaluate(self, piece):
        """Evaluates the board value."""
        neg_piece = self.__get_other_piece(piece)
        score = self.__evaluate_rows(piece, neg_piece)
        if score != 0:
            return self.__zobrist_hash, score
        score = self.__evaluate_cols(piece, neg_piece)
        if score != 0:
            return self.__zobrist_hash, score
        return self.__zobrist_hash, self.__evaluate_diags(piece, neg_piece)

    # ------------------------------------------------------
    def convert_movestring_to_indexes(self, move):
        """Convert the move from the <row><col> format (e.g. "A1")
        format to the board x,y indexes.
        """
        row = move[0].upper()
        col = move[1]
        return self.__convert_move_coords_to_indexes(row, col)

    # ------------------------------------------------------
    def convert_move_to_movestring(self, move):
        """Convert the move from the [x,y] move format
        to the <row><col> string format (e.g. "A1").
        """
        return self.__convert_indexes_to_movestring(move[0], move[1])

    # ------------------------------------------------------
    def __remove_pawn(self, _x, _y):
        """Removes a pawn from the given board position."""
        piece = self.__board[_x][_y]
        if piece != "_":
            self.__update_zhash(_x, _y, piece)
            self.__board[_x][_y] = "_"
        return piece

    # experimental code that try to explore the concept
    # of "equivalent boards"... could be used by learner
    # player to speed up learning. Temporarly disabled...
    # ------------------------------------------------------
    #def get_zhash_equivalent_boards(self):
    #    """Return the zhash of the current board and of all
    #        the equivant simmetrical boards"""
    #    zhash2 = self.__rotate_board_clockwise()
    #    zhash3 = self.__rotate_board_clockwise()
    #    zhash4 = self.__rotate_board_clockwise()
    #    zhash1 = self.__rotate_board_clockwise()
    #    return zhash1, zhash2, zhash3, zhash4

    # ------------------------------------------------------
    #def __replace_pawn(self, _x, _y, piece):
    #    """Replace a pawn in the given board position
    #        with the given piece."""
    #    old_piece = self.__remove_pawn(_x, _y)
    #    self.place_pawn(_x, _y, piece)
    #    return old_piece

    # ------------------------------------------------------
    #def __move_pawn(self, x0, y0, x1, y1):
    #    """Move the pawn in the [x0, y0] position to the
    #       [x1, y1] position. Returns the piece that was
    #       in the [x1, y1] position"""
    #    return self.__replace_pawn(x1, y1, self.__remove_pawn(x0, y0))

    #def __rotate_board_clockwise(self):
    #    """Build the board equivalent to the current one
    #        rotating it by 90 degrees clockwise"""
    #    piece = self.__board[0][0]
    #    piece = self.__replace_pawn(0, 2, piece)
    #    piece = self.__replace_pawn(2, 2, piece)
    #    piece = self.__replace_pawn(2, 0, piece)
    #    _ = self.__replace_pawn(0, 0, piece)
    #    piece = self.__board[0][1]
    #    piece = self.__replace_pawn(1, 2, piece)
    #    piece = self.__replace_pawn(2, 1, piece)
    #    piece = self.__replace_pawn(1, 0, piece)
    #    _ = self.__replace_pawn(0, 1, piece)
    #    return self.__zobrist_hash

    # ------------------------------------------------------
    @staticmethod
    def __convert_move_coords_to_indexes(row, col):
        """Convert move coordinates (e.g. "A","1") to board x,y indexes."""
        row_to_x = {
            "A": 0,
            "B": 1,
            "C": 2
        }
        col_to_y = {
            "1": 0,
            "2": 1,
            "3": 2
        }
        return row_to_x.get(row, -1), col_to_y.get(col, -1)

    # ------------------------------------------------------
    @staticmethod
    def __convert_indexes_to_movestring(_x, _y):
        """Convert the move from board x,y indexes to <row><col> format (e.g. "A1")."""
        x_to_row = {
            0: "A",
            1: "B",
            2: "C"
        }
        y_to_col = {
            0: "1",
            1: "2",
            2: "3"
        }
        mstring = ""
        mstring += x_to_row[_x]
        mstring += y_to_col[_y]
        return mstring

    # ------------------------------------------------------
    def __evaluate_rows(self, pos_piece, neg_piece):
        """Evaluates the board value checking only rows."""
        val = 0
        row = 0
        while val == 0 and row < 3:
            if self.__board[row][0] == self.__board[row][1] and \
                    self.__board[row][1] == self.__board[row][2]:
                if self.__board[row][0] == pos_piece:
                    val = 10
                elif self.__board[row][0] == neg_piece:
                    val = -10
            row += 1

        return val

    # ------------------------------------------------------
    def __evaluate_cols(self, pos_piece, neg_piece):
        """Evaluates the board value checking only columns."""
        val = 0
        col = 0
        while val == 0 and col < 3:
            if self.__board[0][col] == self.__board[1][col] and \
               self.__board[1][col] == self.__board[2][col]:
                if self.__board[0][col] == pos_piece:
                    val = 10
                elif self.__board[0][col] == neg_piece:
                    val = -10
            col += 1

        return val

    # ------------------------------------------------------
    def __evaluate_diags(self, pos_piece, neg_piece):
        """Evaluates the board value checking only diagonals."""
        val = 0
        if self.__board[0][0] == self.__board[1][1] and \
           self.__board[1][1] == self.__board[2][2]:
            if self.__board[1][1] == pos_piece:
                val = 10
            elif self.__board[1][1] == neg_piece:
                val = -10

        if val != 0:
            return val

        if self.__board[0][2] == self.__board[1][1] and \
           self.__board[1][1] == self.__board[2][0]:
            if self.__board[1][1] == pos_piece:
                val = 10
            elif self.__board[1][1] == neg_piece:
                val = -10

        return val

    # ------------------------------------------------------
    def __init_zhash(self, init_zhash):
        """Initialize Zobrist hash table with values provided
        or generating random values."""

        self.zhash_table = np.empty([3, 3, 2], dtype=int)
        if init_zhash is not None:
            for _x in range(0, 3):
                for _y in range(0, 3):
                    for _e in range(0, 2):
                        self.zhash_table[_x][_y][_e] = init_zhash[_x][_y][_e]
        else:
            random.seed()
            for _x in range(0, 3):
                for _y in range(0, 3):
                    for _e in range(0, 2):
                        self.zhash_table[_x][_y][_e] = random.randint(0, sys.maxsize)

        # compute current board Zobrist hash value
        self.__evaluate_zhash()

    # ------------------------------------------------------
    def __evaluate_zhash(self):
        """Completely evaluates Zobrist hash value of the current board."""
        self.__zobrist_hash = 0
        for _x in range(0, 3):
            for _y in range(0, 3):
                piece = self.__board[_x][_y]
                if piece != "_":
                    piece_ndx = self.__convert_piece_in_index(piece)
                    self.__zobrist_hash ^= self.zhash_table[_x][_y][piece_ndx]

    # ------------------------------------------------------
    def __update_zhash(self, _x, _y, piece):
        """Update Zobrist hash value after a board status change
        due to a single place or remove of a pawn.
        """
        piece_ndx = self.__convert_piece_in_index(piece)
        self.__zobrist_hash ^= self.zhash_table[_x][_y][piece_ndx]

    # ------------------------------------------------------
    def __convert_piece_in_index(self, piece):
        """Convert a piece in internal index."""
        if piece == self.__first_piece:
            return 0
        return 1

    # ------------------------------------------------------
    def __get_other_piece(self, piece):
        if piece == self.__first_piece:
            return self.__second_piece
        return self.__first_piece

    # ------------------------------------------------------
    def __str__(self):
        """__str__ display of the board."""
        ###return '     1    2    3\nA %r\nB %r\nC %r\n--- hash = %r' % \
        ###    (self.__board[0], self.__board[1], self.__board[2], self.__zobrist_hash
        return '    1    2    3\nA %r\nB %r\nC %r\n' % \
            (self.__board[0], self.__board[1], self.__board[2])

    # ------------------------------------------------------
    def __repr__(self):
        """__repr__ representation of the board."""
        return 'Board(%s)' % self.__board
