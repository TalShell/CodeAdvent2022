import numpy as np 
import math
import collections as col



def func(s):
    op = s.lstrip().split(' ')
    if op[1]=='*':
        if op[2] == 'old':
            return lambda x : x*x
        return lambda x : x*int(op[2])
 
    if op[1]=='+':
        if op[2] == 'old':
            return lambda x : x+x
        return lambda x : x+int(op[2]) 
    
def test(x,s):
    return int(x%s==0)
    
class Monkey(object):
    def __init__(self, id,items,worry,test,pos_next,neg_next):
        self.id = int(id.split(' ')[1])
        self.items=list(map(int,items.split(',')))
        self.worry = worry
        self.test=int(test)
        self.next=[int(neg_next),int(pos_next)]
        self._inspected = 0

    def __str__(self):
        return f"{self.id} ,{self.items},{self.worry},{self.test}"

    
def day11(path,part1=True,N=20):
    with open(path) as file:
        lines = file.readlines()
    
    operations = []
    monkeys =[]
    for  i in range(0,len(lines),7):
        operations +=[[]]
        mm = lines[i:7+i]
        #print(mm)
        M = Monkey(mm[0].strip().split(":")[0],
                   mm[1].strip().split(":")[1],
                   mm[2].strip().split("=")[1],
                   mm[3].strip().split("divisible by")[1],
                   mm[4].strip().split("throw to monkey")[1],
                   mm[5].strip().split("throw to monkey")[1])
        #print(M)
        monkeys.append(M)
    for m in monkeys:
        print(m)
        #if m.id == 0:
            #continue
            #m.items.pop()
        #else:
        #    while m.items:
                #print('pop')
                #m.items.pop()
                
        #print("Monkey: ",m)
    #print([len(x.items) for x in monkeys])
    for k in range(N):
        #list_items =[[] for _ in len(monkeys)]
        for m in monkeys:
            m._inspected +=len(m.items)
            while m.items:
                i = m.items.pop()
                #print("Pop ",i)
                roundworr = func(m.worry)(i)
                if part1:
                    roundworr //=3
                else:
                    roundworr= roundworr % (11*13*2*5*7*17*19*3)
                t = test(roundworr,m.test)
                #print(new_worr,roundworr,"throw to ",t,m.next[t])
                monkeys[m.next[t]].items.append(roundworr)
            #print("Next ", monkeys[m.next[t]])
            #print("round: ",k)
        activity =[m._inspected for m in monkeys]
    print("->>> k",k , "---",activity,sum(activity))
    activity.sort(reverse=True)
    print(f"Prod: {part1} ",activity[0]*activity[1])


if __name__=="__main__":
    path ="./1.in"
    day11(path,part1=True,N=20)
    day11(path,part1=False,N=10000)
