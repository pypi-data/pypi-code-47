# --------------------------------------------------------------------
# jokettt project, v. 0.1
# by F. Piantini <francesco.piantini@gmail.com>
# ---
# Tic Tac Toe "Learner" Player class definition
# --------------------------------------------------------------------
"""Implementation of a "learner" tic-tac-toe player, that improves
    his gameplay learning during games.
    The player made use of a value function that assign a value to
    every board state. Initially the value is 0 for any losing position,
    1 for every winning position and 0.5 for all the other positions.
    During games the values of the intermediates position are calibrated
    using the standard reinforcement learning formula:
        V(s) = V(s) + alpha * [ V(s') - V(s) ]
    This class is derived from the Player base class
"""
from random import shuffle

from jokettt.board import Board
from jokettt.player import Player

class LearnerPlayer(Player):
    """A Tic Tac Toe learner automatic player."""

    # --------------------------------------------------------------
    def __init__(self, piece, board, init_values={}, alpha=0.1, verbosity=0):
        """LearnerPlayer class constructor. Save the given piece,
            the alpha value and initializes Value vector."""
        Player.__init__(self, piece, verbosity)
        self.__alpha = alpha

        self.values = init_values
        self.__best_value = -1000
        self.__best_x = None
        self.__best_y = None
        self.__best_zhash = -1
        zhash, score = board.evaluate(self.piece)
        if not zhash in self.values:
            if score > 0:
                # winning board...
                self.values[zhash] = 1.0
            elif score < 0:
                #losing board
                self.values[zhash] = 0.0
            else:
                # playable board
                self.values[zhash] = 0.5
        self.__last_zhash = zhash

    # --------------------------------------------------------------
    def move(self, board):
        """Do a move using reinforcement learning algo"""
        return self.__find_rl_move(board)

    # --------------------------------------------------------------
    def learn_from_defeat(self, board):
        """Updates the value vector given a final lost position"""
        ###zhash = board.get_zhash()
        zhash, score = board.evaluate(self.piece) # score should be negative...
        if score < 0:            # so this check is useless...
            # defeat...
            self.values[zhash] = 0.0
            self.values[self.__last_zhash] += \
            self.__alpha * (self.values[zhash] - \
                            self.values[self.__last_zhash])
            self.log_info("LEARNED FROM DEFEAT... new value for last position: ",
                          self.values[self.__last_zhash])

    # --------------------------------------------------------------
    def __find_rl_move(self, board):
        """Find a move that is considered the best depending on current knowledge"""
        zhash, value = board.evaluate(self.piece)
        # value should be zero, otherwise the game is completed
        if value != 0:
            return None, None

        if not zhash in self.values:
            # the board status is not in values array:
            # this is the first time we encounter this position
            self.log_info("new board status encounted: init to 0.5")
            self.values[zhash] = 0.5

        move_list = board.valid_moves()
        # interestingly, if we shuffle the possible moves before to select them,
        # the learning playing against a minimax player is slower
        shuffle(move_list)  # to add some variability to the play (...maybe)

        self.__best_value = -1000
        self.__best_x = None
        self.__best_y = None
        for move in move_list:
            if self.__analyze_move(move, board):
                # winning move found
                break

        # move selected... updates current zhash
        self.values[zhash] += \
            self.__alpha * (self.values[self.__best_zhash] - \
                            self.values[zhash])
        self.values[self.__last_zhash] += \
            self.__alpha * (self.values[self.__best_zhash] - \
                            self.values[self.__last_zhash])

        self.log_info("Position value updated. New value = ", self.values[zhash])

        self.__last_zhash = self.__best_zhash
        return self.__best_x, self.__best_y

    # --------------------------------------------------------------
    def __analyze_move(self, move, board):
        """Analyze the move "move" given the current "board" status
            Returns True if the move is winning"""

        # do the move. The analyze_move() method returns the zhash
        # and the score of the board after the given move.
        # The score can be > 0 if the move is winning, or 0 if
        # the move does not cause a win.
        # Note that it is impossible that the score is < 0: it is
        # impossible to enter in lost position when it is our turn
        # to move
        zhash, score = board.analyze_move(move, self.piece)
        self.log_info("evaluating move: ", board.convert_move_to_movestring(move),
                      ", score = ", score, ", zhash = ", zhash)

        if score > 0:
            # we win! choose this move
            self.log_info("WINNING MOVE! Choose it")
            self.values[zhash] = 1.0
        else:
            # neutral move... if the hash is not in dictionary
            # this is the first time we encounter this move:
            # initialize value
            self.log_info("NEUTRAL MOVE... analyzing it")
            if not zhash in self.values:
                self.log_info("   - new board status encounted: init to 0.5")
                self.values[zhash] = 0.5
            else:
                self.log_info("   - I know this move... value = ", self.values[zhash])

        # It the value of the board after the move is better of values
        # seen until now, save the move data
        if self.__best_value < self.values[zhash]:
            self.__best_zhash = zhash
            self.__best_value = self.values[zhash]
            self.__best_x, self.__best_y = move
            self.log_info("   - move is selected as the new best choice - value = ",
                          self.__best_value)

        return score > 0
