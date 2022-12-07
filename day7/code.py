import numpy as np
import collections as col


def q1(dirs):
    print("Q1:|-----------> ")
    size_subs(dirs,all_dirs[0])
    total=0
    atmost =100000
    for d in all_dirs:
        if d.type=="dir":
            print(d.name,d.size)
            if d.size <= atmost:
                total+=d.size
                print('OK')
    print('Total: ',total)
    print("Q1:<-----------| ")


def q2():
    totalspace = 70000000
    update = 30000000
    unused_space = totalspace - all_dirs[0].size
    lowest_space = update-unused_space
    print(lowest_space)
    lowest_size =all_dirs[0].size
    for d in all_dirs:
        if d.size<lowest_space or d.type=='file':
            continue
        else:
            lowest_size = min(lowest_size,d.size)
    print(lowest_size)

    pass


def command(l, visited_dirs):
    content = False

    if l[1] == "cd":
        if l[2] == "..":
            visited_dirs.pop()
        else:
            visited_dirs.append(l[2])
    elif l[1] == "ls":
        content = True
    return visited_dirs, content


all_dirs = []
all_sizes={}

class Smth:
    def __init__(self, type, name):
        if "dir" in type:
            self.type = type
            self.size = 0
        else:
            self.type = "file"
            self.size = int(type)
            all_sizes[name]=self.size

        self.name = name

    def __str__(self):
        return f"{self.type} , {self.name} , {self.size}"

def size_subs(dirs,x,size=0):	
	if x.type=='file':
		return x.size
	
	x.size=0
	for e in dirs[x.name]:
		if e.type =="file":
			x.size +=e.size
		else:
			e.size=size_subs(dirs,e)
			x.size +=e.size
	return x.size

def key(l):
    return '#'.join(l)
def main():
    path = "./in"
    with open(path) as file:
        lines = file.readlines()
    dirs = {}
    visited_dirs = []
    content = False
    root = Smth('dir','/')
    all_dirs.append(root)
    for l in lines:
        if "$" in l:
            c = l.strip("\n").split(" ")
            visited_dirs, content = command(c, visited_dirs)
            if key(visited_dirs) not in dirs:
                dirs[ key(visited_dirs)]=[]

        if content and ("$" not in l):
            f = l.strip().split(" ")
            s=Smth(f[0],key(visited_dirs)+'#'+f[1])
            dirs[ key(visited_dirs)].append(s)
            all_dirs.append(s)

    q1(dirs)
    q2()
if __name__ == "__main__":
    main()
