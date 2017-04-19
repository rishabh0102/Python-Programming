##
## Part III: Connect Four Play
##

import random

from board import Board
from hw06_2 import Player


def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
            or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)

    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board


##
## Problem 6.3a) process_move
##

def process_move(player, board):
    """
        This method accepts a board object and a player object as parameters
        and returns whether the game is over after the player makes his next move.
        Meanwhile, it also updates the board.
     """
    # Printing the players turn using __repr__ method of Player class
    print (str(player) + "'s turn")
    # Asking the user for the next move
    col_entered = player.next_move(board)
    # Adding the next move of the player to the board
    board.add_checker(player.checker, col_entered)

    print ('-----------------------')
    print (board)

    # Checking if the player has won
    if board.is_win_for(player.checker):
        print (str(player).__add__(" wins in " + str(player.num_moves) + " moves"))
        print ("Congratulations!")
        return True
    # If not won, then it can be a tie when no more moves can be made.
    else:
        for x in range(0, board.width):
            if board.can_add_to(x):
                # If any move can be made, return False because the game is not yet over.
                return False
    # If no more moves can be made, the game is over and it's a tie
    print ("It's a tie!")
    return True


##
##  Problem 6.3b) RandomPlayer
##


class RandomPlayer(Player):
    def next_move(self, board):
        # List of all the columns which allow another checker
        valid_cols = []

        for col in range(0, board.width):
            # Checks which columns are not full i.e they allow another checker.
            if board.can_add_to(col):
                valid_cols.append(col)
        """
        While the valid column doesn't come, it shall continue to run
        """
        # Random value for the between 0 and number 0f valid columns -1
        random_value = random.randint(0, len(valid_cols) - 1)
        # We now get the random move made by the RandomPlayer
        move = valid_cols[random_value]
        """
         If the input is valid, we now see if we can
         play the move. We first ask the board's inbuilt function
        """
        # Update the self number of moves.
        self.num_moves += 1
        """ After the appropriate move is found, we just return it """
        # Return the move value.
        return move


from hw06_2 import Player
from hw06_3 import RandomPlayer, connect_four
from board import Board
from hw06_3 import process_move



#test case

def test_third_part():
    playing_board = Board(2,4) # Initializing the board so that the player can play.
    print (playing_board) # Testing the empty board
    playing_board.add_checkers('001212') # Adding the checkers to test the method and prepare the board for testing process_move!
    print (playing_board)
    process_move(Player('X'),playing_board)
    print ('-------------------------------')
    print ('Let us test it again')
    playing_board = Board(2,4) # Cleaning the board for another test.
    playing_board.add_checkers('0011232')  # Adding the checkers to test the method and prepare the board for testing process_move!
    print (playing_board)
    process_move(Player('O'), playing_board)

    random_player = RandomPlayer('X') # Testing the intialization of RandomPlayer class
    print (random_player) # Testing the inherited __repr__ function of PLayer class.
    print (random_player.opponent_checker()) # Testing the opponent_checker method for RandomPlayer class
    playing_board = Board(2, 4)  # Cleaning the board for another test.
    playing_board.add_checkers('001223')
    print (playing_board)

    # In all the next four calls, it should print (only 1 or 3 because those are only two columns left for the next move.
    print ('next_move',random_player.next_move(playing_board)) # Checking the random moves of the RandomPlayer
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer

    playing_board.add_checker('X',3) # adding another checker to the board
    print ('--------------')
    print (playing_board)
    print ('Next moves after adding another checker at column 3')
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer
    print ('next_move',random_player.next_move(playing_board))  # Checking the random moves of the RandomPlayer


    pass


    connect_four(Player('X'), RandomPlayer('O')) # Playing against a Random player
    connect_four(RandomPlayer('X'), RandomPlayer('O')) # A match between two Random players


if __name__ == '__main__':
    test_third_part()


