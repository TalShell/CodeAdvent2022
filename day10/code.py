import numpy as np 
import math
import collections as col

def q1(progs):
    X = 1
    log=[X]
    for p in progs:
        if p[0]=='noop':
            log+=[X]
        else:
            log+=[X]
            X +=int(p[1])
            log+=[X]  
    print(log[19],log[59],log[99],log[139],log[179],log[219])
    total = 20*log[19]+60*log[59]+100*log[99]+140*log[139]+180*log[179]+220*log[219]
    print(total)

def main():
	path = "./1.in"
	with open(path) as file:
		lines = file.readlines()

	progs = [l.strip('\n').split(' ') for l in lines]
	q1(progs)
if __name__=="__main__":
	main()
