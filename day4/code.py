import numpy as np 
import collections as col

'''


'''
def overlap(ass):
	p1 = [int(x) for x in ass[0].split('-')]
	p2 = [int(x) for x in ass[1].split('-')]
	inter = set(range(p1[0],p1[1]+1)).intersection(set(range(p2[0],p2[1]+1)))
	if len(inter) >0:
		print(p1, p2 ,inter)

		return 1
	return 0

def is_incl(ass):
	p1 = [int(x) for x in ass[0].split('-')]
	p2 = [int(x) for x in ass[1].split('-')]
	m = min(len(set(range(p1[0],p1[1]+1))),len(set(range(p2[0],p2[1]+1))))
	inter = set(range(p1[0],p1[1]+1)).intersection(set(range(p2[0],p2[1]+1)))
	print(inter)
	if len(inter) == m:
		print(p1, p2 ,inter,m)

		return 1
	return 0

def q1(asss):
	inclus = 0
	for s in asss:
		inclus +=is_incl(s)
	print(inclus)
	return inclus
	

def q2(asss):
	inclus = 0
	for s in asss:
		overlap +=overlap(s)
	print(inclus)
	return inclus

def main():
	#path = str(input())
	path="./in"
	with open(path) as file:
		lines = file.readlines()
	assignements=[]
	for l in lines:
		assignements.append(l.strip('\n').split(','))
	print(assignements)
	q1(assignements)

if __name__=="__main__":
	main()
