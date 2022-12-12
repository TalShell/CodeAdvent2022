import numpy as np
import collections as col


def printg(grid):
    for l in grid:
        print(l)
N=10
grid = [['.' for _ in range(N)] for _ in range(N)]
directions = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1],
              'UL':[-1,-1],'UR':[-1,1],'DL':[1,-1],'DR':[1,1]}

def d(l,k):
    print(l,k)
    return (l[0]-k[0])*(l[1]-k[1])


    #print(new_h,new_t)
    

def main():
    path = "./t.in"
    with open(path) as file:
        lines = file.readlines()
    xmp = [ l.strip('\n').split(' ') for l in lines]
    t_pos=[[0,0]]
    h_pos=[[0,0]]
    print(xmp)
    for x in xmp:
        h = h_pos[-1]
        t = t_pos[-1]
        dr = x[0]
        c = 0
        print(x)
        while c <int(x[1]):
            h = h_pos[-1]
            new_t = t_pos[-1]
            new_h = [h[0]+directions[dr][0],h[1]+directions[dr][1]]
            if t==h:
                print('same!')
                h = new_h
            else:
                dis =d(new_t,new_h)
                print(">>>>>>> ",dis)
                if dis !=0:
                    if new_h[0]-new_t[0] >0: #D
                        print("---> D")
                        if new_h[1]-new_t[1]>0: #R
                            print("-----> R")

                            new_t = [new_t[0]+directions['DR'][0],new_t[1]+directions['DR'][1]]
                        else: #L
                            print("-----> L")

                            new_t = [new_t[0]+directions['DL'][0],new_t[1]+directions['DL'][1]]
                    else: #U
                        print("---> U")

                        if new_h[1]-new_t[1]>0: #R
                            print("-----> R")

                            new_t = [new_t[0]+directions['UR'][0],new_t[1]+directions['UR'][1]]
                        else: #L
                            print("-----> L")

                            new_t = [new_t[0]+directions['UL'][0],new_t[1]+directions['UL'][1]]                        
                else:
                    new_t = [new_t[0]+directions[dr][0],new_t[1]+directions[dr][1]]
                    print("new_t ",new_t)
            h_pos.append(new_h)
            t_pos.append(new_t)
            c +=1
    set_key=[str(x[0])+'#'+str(x[1]) for x in t_pos]
    print(set(set_key))
if __name__ == "__main__":
    main()
