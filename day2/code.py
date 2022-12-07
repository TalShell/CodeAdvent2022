import numpy as np 
import math
import collections as col

'''

A for Rock, B for Paper, and C for Scissors.
X for Rock, Y for Paper, and Z for Scissors. 

Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score.
 Your total score is the sum of your scores for each round.
 The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
  plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get 
if you were to follow the strategy guide.


'''
dict_loss={'A':'Z','B':'X','C':'Y'}
dict_ations={'A':'Y','B':'Z','C':'X'}
dict_similar ={'A':'X','B':'Y','C':'Z'}
choices_scores= {'X':1,'Y':2,'Z':3}
opp_scores= {'A':1,'B':2,'C':3}

WIN = 6
LOSS =0
DRAW =3
how_should={'X':LOSS,'Y':DRAW,'Z':WIN}

'''
For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score 
	of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

'''

def win_loss(r):
	print(r)
	score = choices_scores[r[1]]
	if dict_ations[r[0]] == r[1]:
		score +=WIN
	elif dict_similar[r[0]]==r[1]:
		score +=DRAW
	print(score)
	return score

def outcome(round):
	score =0
	for r in round:
		print(r)
		score +=win_loss(r)
	return score

def score_from_outcome(round):
	score = how_should[round[1]]

	if score == WIN:
		score +=choices_scores[dict_ations[round[0]]]
		print(round," WIN >> score ",score, dict_ations[round[0]] )
	elif score ==DRAW:
		score +=opp_scores[round[0]]
		print(round," DRAW >> score ",score, dict_similar[round[0]] )

	else:
		score +=choices_scores[ dict_loss[round[0]]]
		print(round, " LOSS: ",score, round[0],dict_loss[round[0]])

	return score

def main():
	#path = str(input())
	path="./in"
	choices = []
	with open(path) as file:
		lines = file.readlines()

	for l in lines:
		choices.append(l.strip("\n").split(" "))
	
	print(choices)
	print(outcome(choices))
	all = 0 
	for r in choices:
		all +=score_from_outcome(r)
	print(all)



if __name__=="__main__":
	main()
