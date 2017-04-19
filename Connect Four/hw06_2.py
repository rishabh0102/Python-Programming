
##
## Part II: Connect Four Setup
##


##
## Problem 6.2) A Connect Four Player class
##

class Player:
    """ a class representing a player that plays the Connect Four Game
    """

    def __init__(self, checker):
        """
        This is the constructor that construct a player object with the character passed int the checker variable
        """

        """
        The num_moves stores the number of moves the player has played so far, hence initialized to 0
        """

        self.checker = checker
        self.num_moves = 0

    """ This funtion creates a string representation
        of the object
    """

    def __repr__(self):
        return "Player " + str(self.checker)

    """ This function returns a character showing the
        checker of the opponent (uppercase)
    """

    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    """ This method accepts a board object as a paramenter
        and returns the column number where the player want to
        make the next move.
    """

    def next_move(self, board):
        valid = False

        """ While the player doesn't do a valid move
            ask the player for a new move and converts it
            into an integer variable
        """
        while not valid:
            move = int(input("Enter a column: "))

            """ If the input is valid, we now see if we can
                play the move. We first ask the board's inbuilt function
            """
            if board.can_add_to(move):
                valid = True
                self.num_moves += 1
            else:
                print("Try again!")

        """ After the appropriate move is found, we just return it """
        return move



from hw06_2 import Player
from board import Board

#test case


def test_second_part():
    player_first = Player('X')
    print (player_first.checker) # Tests that the checker variable has been initiated by the constructor.
    print (player_first.num_moves) # Tests that the num_moves variable has been initiated by the constructor.
    print (player_first)  # Tests the __repr__ method.
    print (type(player_first.__repr__())) # Confirm that the method indeed returns a String.
    print (player_first.opponent_checker()) # Confirms the right functionality of the opponent_checker method
    playing_board = Board(6,7) # Initialises a board object for testing the next_move method of Player Class
    print (player_first.next_move(playing_board)) # Asks the user for the next move and checks the complete functionality of the next_move function.

# if __name__ == '__main__':
#     test_second_part()