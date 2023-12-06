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
    time_value = line1[1].strip().replace(" ", "")
    distance_value = line2[1].strip().replace(" ", "")
    beats=0
    loading_time=0
    for i in range(int(time_value)):
        speed=acceleration*loading_time
        distance=speed*(int(time_value)-loading_time)
        if distance>int(distance_value):
            beats+=1
        loading_time += 1
    result=0
    print(beats)
