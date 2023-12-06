import numpy as np


def read_input(filename):
    with open(filename) as f:
        ret = f.readlines()
    return ret
acceleration = 1#1mm per 1ms
if __name__ == '__main__':
    file=read_input("text.txt")
    line1 = file[0].split(":")
    line2 = file[1].split(":")
    time_values = line1[1].strip().split()
    distance_values = line2[1].strip().split()
    beats=np.zeros(len(time_values))
    for i in range(len(time_values)):
        loading_time=0
        for j in range(int(time_values[i])):
            speed=acceleration*loading_time
            distance=speed*(int(time_values[i])-loading_time)
            if distance>int(distance_values[i]):
                beats[i]+=1
            loading_time += 1
    result=1
    for i in beats:
        result=+result*int(i)
    print(result)
