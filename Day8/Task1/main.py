
def read_input(filename):
    with open(filename) as f:
        ret = f.readlines()
    return ret
steps=[]
dictionary={}
position="AAA"
result=0
if __name__ == '__main__':
    file = read_input("text.txt")
    for i in range(len(file)):
        if i==0:
            steps=file[i].replace("R", "1").replace("L", "0").replace("\n", "")
        line = file[i].split(' = ')
        if i>1:
            current=line[0]
            tup=line[1].replace("\n", "").replace("(", "").replace(")", "").split(", ")
            dictionary[current] = tuple(tup)
    reps=0
    while position != "ZZZ":
        for turn in range(len(steps)):
            result += 1
            position=dictionary[position][int(steps[turn])]
        reps+=1
    print("results: ")
    print(result)


