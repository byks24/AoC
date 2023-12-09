import numpy as np


def read_input(filename):
    with open(filename) as f:
        ret = f.readlines()
    return ret


def create_subarray(arr):
    sub_arr = np.zeros(len(arr) - 1, dtype=int)
    for i in range(len(arr) - 1):
        sub_arr[i] = int(arr[i + 1]) - int(arr[i])
    return sub_arr


result = 0

if __name__ == '__main__':
    file = read_input("text.txt")
    for i in range(len(file)):
        index = 0
        steps = []
        line = file[i].replace("\n", "").split()
        array = np.array(line, dtype=int)
        steps.append(array)
        while np.count_nonzero(steps[index]) != 0:
            steps.append(create_subarray(steps[index]))
            index += 1
        steps.reverse()
        for j in range(len(steps)):
            if j == 0:
                steps[j] = np.append(steps[j], 0)
            elif j == len(steps) - 1:
                result += steps[j][-1] + steps[j - 1][-1]
            else:
                steps[j] = np.append(steps[j], (steps[j][-1] + steps[j - 1][-1]))
    print("results: ")
    print(result)
