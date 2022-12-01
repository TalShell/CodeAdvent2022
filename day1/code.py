import numpy as np 
import math
import collections as col

'''
The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; 
the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin 
taking inventory of their supplies. One important consideration is food - in particular, 
the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks,
rations, etc. that they've brought with them, one item per line. Each Elf separates their own 
inventory from the previous Elf's inventory (if any) by a blank line.

'''


def elves_assets(lines):
	elves={}
	nb_elf=0
	calories=0
	for i,l in enumerate(lines):
		if l!='\n':
			calories +=int(l)
		if l=='\n' or i == len(lines)-1:
			elves[nb_elf]=calories
			calories = 0
			nb_elf +=1
	elves = sorted(elves.items(), key=lambda x: x[1],reverse=True)
	print(elves)
	return elves

def max_calories(lines):
	elves = elves_assets(lines)
	return(next(iter(elves))[1])

def top_three(lines):
	elves = elves_assets(lines)
	top3 = 0
	s=0
	iterElv =iter(elves)
	while top3<3:
		s +=next(iterElv)[1]
		top3 +=1
		print(s, top3)
	return s

def main():
	path = str(input())
	with open(path) as file:
		lines = file.readlines()

	print("Max_calories: ",max_calories(lines))
	print("Top3: ",top_three(lines))

if __name__=="__main__":
	main()
