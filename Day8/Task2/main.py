import numpy as np
import math

def read_input(filename):
    with open(filename) as f:
        ret = f.readlines()
    return ret
steps=[]
dictionary={}
position=[]
result=0
if __name__ == '__main__':
    file = read_input("text.txt")
    for i in range(len(file)):
        if i==0:
            steps=file[i].replace("R", "1").replace("L", "0").replace("\n", "")
        line = file[i].split(' = ')
        if i>1:
            current=line[0]
            if current[2]=="A":
                position.append(current)
            tup=line[1].replace("\n", "").replace("(", "").replace(")", "").split(", ")
            dictionary[current] = tuple(tup)
    reps=np.zeros(len(position), dtype=int)
    index=0
    for i in position:
        while i[2] != "Z":
            for turn in range(len(steps)):
                result += 1
                i = dictionary[i][int(steps[turn])]
                reps[index] += 1
        index+=1

    print("reps: ")
    print(reps)
    print("results: ")
    print(math.lcm(*reps))


