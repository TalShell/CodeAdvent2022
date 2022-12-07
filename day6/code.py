import numpy as np 
import collections as col


def q1(crates):
	pass
	

def q2(crates):
	pass

def all_dif(l):
	#print(l)
	return len(set(l))==len(l)

def find_start(s):
	pos = 0
	for i in range(0,len(s)):
		if all_dif(s[i:i+14]):
			print(i+14)
			break
		else:
			pos +=4

def main():
	#path = str(input())
	path="./in"
	with open(path) as file:
		lines = file.readlines()
	
	streams=[]
	for l in lines:
		stream = l.strip('\n')
		print(stream)
		find_start(stream)
if __name__=="__main__":
	main()
