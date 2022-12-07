import numpy as np 
import collections as col

'''


'''

def q1(crates):
	pass
	

def q2(crates):
	pass

def move(stacks,q, fro,to):
	c=0
	while c <q:
		stacks[to].append( stacks[fro].pop())
		c +=1
		print(stacks[fro],stacks[to])
	return stacks

def move9001(stacks,q, fro,to):
	c=len(stacks[fro])
	print(stacks[to], '->')
	stacks[to] +=stacks[fro][c-q:c]
	c=0
	while c <q:
		stacks[fro].pop()
		c+=1
	print(stacks[to])
	return stacks
def main():
	#path = str(input())
	path="./in"
	with open(path) as file:
		lines = file.readlines()

	'''
	[D]    
	[N] [C]    
	[Z] [M] [P]
	1   2   3 
	'''
	#stacks = [[],['Z','N'],['M','C','D'],['P']]
	'''
		[W]         [J]     [J]        
		[V]     [F] [F] [S] [S]        
		[S] [M] [R] [W] [M] [C]        
		[M] [G] [W] [S] [F] [G]     [C]
	[W] [P] [S] [M] [H] [N] [F]     [L]
	[R] [H] [T] [D] [L] [D] [D] [B] [W]
	[T] [C] [L] [H] [Q] [J] [B] [T] [N]
	[G] [G] [C] [J] [P] [P] [Z] [R] [H]
	1   2   3   4   5   6   7   8   9 
	'''
	stacks=[[],['G','T','R','W'],['G','C','H','P','M','S','V','W'],
		['C','L','T','S','G','M'],['J','H','D','M','W','R','F'],['P','Q','L','H','S','W','F','J'],
		['P','J','D','N','F','M','S'],['Z','B','D','F','G','C','S','J'],['R','T','B'],['H','N','W','L','C']]
	print(stacks)
	for l in lines:
		if 'move ' in l:
			m=int(l.split('from')[0].strip('move '))
			#print(m)
			f =l.split('from')[1]
			f = f.strip('\n').split('to')
			f = [int(x.strip()) for x in f]
			#print(f)
			#print(l)
			stacks =move9001(stacks,m,f[0],f[1])
			print(stacks)
	word=[]
	for s in stacks:
		if  s:
			word.append(s.pop())
	print(''.join(word))

if __name__=="__main__":
	main()
