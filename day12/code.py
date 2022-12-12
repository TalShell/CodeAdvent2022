import numpy as np 
import math
import collections as col


def heat(x):
	return ord(x)-96

def neighbours(grid,x):
	ops = [[0,1],[-1,0],[0,-1],[1,0]]
	potential = [[x[0]+o[0],x[1]+o[1]] for o in ops]	
	neg = []
	for p in potential:
		if p[0]<0 or p[1]<0 or p[0]> len(grid)-1 or p[1]>len(grid[0])-1:
			continue
		neg.append(p)
	return neg

def explore(grid,s,E,q=[],v=[]):
	q +=[s]
	v+=[grid[s[0]][s[1]]]
	print(v)
	print("S,E",s,E)
	if s[0]==E[0] and s[1]==E[1]:
		print("SOLVED",q, len(q),v)
		return q

	neig = neighbours(grid,s)
	maxz = max([grid[n[0]][n[1]] if grid[n[0]][n[1]]<=grid[s[0]][s[1]]+1 else 0 for n in neig ])
	print("NEEEG ",maxz)
	add = False
	for n in neig:
		if grid[n[0]][n[1]] - grid[s[0]][s[1]] >1 or grid[n[0]][n[1]] - grid[s[0]][s[1]] <0 :
			#print(n ,  grid[n[0]][n[1]],'Then ',grid[s[0]][s[1]] , "Continue")
			continue
		else:
			print(f"ELSE {s} -> {n} ",grid[s[0]][s[1]],grid[n[0]][n[1]])
			if  n not in q and grid[n[0]][n[1]]==maxz:
				#print(n ,  grid[n[0]][n[1]],'Then ',grid[s[0]][s[1]] , "else", q,len(q))
				q += explore(grid,n,E,q)
				add=True
	if not add:
		q.pop()
		v.pop()
	return q

def main():
	#path = str(input())
	path="./t.in"
	with open(path) as file:
		lines = file.readlines()

	grid= [[x for x in l.strip()] for l in lines]
	for g in grid:
		print(g)
	ngrid=[list(map(heat,g)) for g in grid]

	S=[0,0]
	E=[2,5]
	ngrid[0][0]=heat('a')
	ngrid[2][5]=heat('z')

	print(np.asarray(ngrid))
	q = []
	visited =[S]
	while False:
		if not q:
			break
		p = q.pop()
		visited.append(p)
		if p==E:
			q.append(p)
			print("END")
			break
		neg = neighbours(ngrid,p)
		for n in neg:
			if ngrid[n[0]][n[1]] - ngrid[p[0]][p[1]]>=1:
				print(n ,  ngrid[n[0]][n[1]], 'Then ',ngrid[p[0]][p[1]] , "Continue")
				print(q,)
				continue
			if n not in visited :
				q.append(n)
	
	#print(neighbours(ngrid,S))
	explore(ngrid,S,E)
if __name__=="__main__":
	main()
