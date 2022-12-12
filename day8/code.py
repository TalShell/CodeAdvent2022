import numpy as np
import collections as col

def is_visible(F,i,k):
    TF=F.T
    r = F[i][k] > np.max(F[i][:k]) or F[i][k] > np.max(F[i][k+1:]) or TF[k][i] > np.max(TF[k][:i]) or TF[k][i] > np.max(TF[k][i+1:]) 
    #print(r, F[i][k] , np.max(F[i][:k]),F[i][:k] , F[i][k+1:] , TF[k][i] ,TF[k][:i], np.max(TF[k][:i]),TF[k][i+1:] , np.max(TF[k][i+1:]))
    return r 

def q1(forest):
    F=np.asarray(forest)
    print(F)
    visible = (len(F)-1)*4
    for i,r in enumerate(F):
        for k,_ in enumerate(r):
            if i*k==0 or i==len(F)-1 or k ==len(F)-1:
                continue
            if is_visible(F,i,k) :
                visible +=1
    print(visible)

def count(npa):
    c = 0
    for a in npa:
        if a>=0:
            c+=1
            return c
        c+=1
    return c
def scenic_score(F,i,k):
    TF=F.T
    visibility =0
    left = np.flip(F[i][:k]-F[i][k])
    right = F[i][k+1:]-F[i][k]
    top = np.flip(TF[k][:i] -TF[k][i])
    down = TF[k][i+1:]-TF[k][i]
    print(F[i][k],TF[k][i])
    print(F[i][:k], left,count(left))
    print(F[i][k+1:],right ,count(right))
    print( TF[k][:i],top,count(top)) 
    print( TF[k][i+1:],down ,count(down))
    visibility = count(right)*count(left)*count(down)*count(top)
    print(visibility)
    return visibility

def q2(forest):
    F=np.asarray(forest)
    max_c=0
    for i,r in enumerate(F):
        for k,_ in enumerate(r):
            if i*k==0 or i==len(F)-1 or k ==len(F)-1:
                continue
            max_c = max(max_c,scenic_score(F,i,k))
                
    print(max_c)

def main():
    path = "./in"
    with open(path) as file:
        lines = file.readlines()
    forest = [[int(x) for x in l.strip('\n')] for l in lines]
    print(forest)
    q1(forest)
    q2(forest)   
if __name__ == "__main__":
    main()
