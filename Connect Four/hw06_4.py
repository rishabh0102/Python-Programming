##
## Part IV: AI Player
##

import random  
from hw06_3 import *

##
## Problem 6.4) AIPlayer
##

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here """
        super().__init__(checker)
        self.tiebreak =tiebreak
        self.lookahead =lookahead



    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        return "Player " + str(self.checker)+" ("+self.tiebreak+", "+str(self.lookahead)+")"

    def max_score_column(self,scores):
    	max_score = max(scores)
    	list_index = []
    	for x in range(0,len(scores)):
    		if scores[x] == max_score:
    			list_index.append(x)
    			pass
    	if self.tiebreak=='LEFT':
    		return min(list_index)
    		pass
    	elif self.tiebreak=='RIGHT':
    		return max(list_index)
    		pass
    	else:
    		return random.choice(list_index)
    		pass

    def scores_for(self,board):
    	score = [0]*board.width

    	for x in range(0,board.width):
    		if board.can_add_to(x)== False:
    			score[x] = -1
    			pass
    		elif board.is_win_for((self.checker)) == True:
    			score[x] = 100
    			pass
    		elif board.is_win_for(self.opponent_checker()) ==True:
    			score[x] = 0
    			pass
    		elif self.lookahead == 0:
    			score[x] = 50
    			pass
    		else:
    			board.add_checker((self.checker),x)
    			# print(board)
    			opponent = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1)
    			opponent_score = opponent.scores_for(board)
    			if max(opponent_score)==0:
    				score[x] = 100
    				pass
    			elif max(opponent_score)==100:
    				score[x] = 0
    				pass
    			else:
    				score[x] = 50
    				pass
    			board.remove_checker(x)

    	return score

    def next_move(self,board):
    	score_list = self.scores_for(board)
    	move = self.max_score_column(score_list)
    	self.num_moves+=1
    	return move
    	pass



# print(a.scores_for(b))
# print(AIPlayer('O', 'LEFT', 1).scores_for(b))
# print(AIPlayer('X', 'LEFT', 1).scores_for(b))
# print(AIPlayer('X', 'LEFT', 2).scores_for(b))
# print(AIPlayer('X', 'LEFT', 3).scores_for(b))
# print(AIPlayer('O', 'LEFT', 3).scores_for(b))
# print(AIPlayer('O', 'LEFT', 4).scores_for(b))
# print(AIPlayer('X', 'LEFT', 1).next_move(b))
# print(AIPlayer('X', 'RIGHT', 1).next_move(b))
# print(AIPlayer('X', 'LEFT', 2).next_move(b))
# print(AIPlayer('X', 'RIGHT', 2).next_move(b))
# print(AIPlayer('X', 'RANDOM', 2).next_move(b))
# connect_four(Player('X'), AIPlayer('O', 'RANDOM', 3))
# connect_four(Player('X'), Player('O'))
# connect_four(Player('X'), RandomPlayer('O')) # Playing against a Random player
connect_four(Player('X'), AIPlayer('O', 'RANDOM', 4))





