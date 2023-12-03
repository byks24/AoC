import numpy as np

def checkIfNumber(arr, i, j):
    if arr[i][j].isdigit():
        return True
    else:
        return False
def getNumber(arr, i, j, arraySize):
    string = ''
    len = 0
    while j+len < arraySize and arr[i][j+len].isdigit():
        string += arr[i][j+len]
        len += 1
    return int(string), len
def checkSurrounding(arr, i, j, number):
    isPart = False
    for ii in range(i-1, i+2):
        for jj in range(j-1, len(str(number)) + j + 1):
            if ii < 0 or ii >= arr.size or jj < 0 or jj >= len(array[i]) or (ii==i and jj in range(j,j+len(str(number)))):
                continue
            else:
                if arr[ii][jj] != '.':
                    isPart = True
    return isPart

if __name__ == '__main__':
    skip=0
    result = 0
    array = np.genfromtxt("text.txt", dtype=str, comments="Comment")

    for i in range(array.size):
        for j in range(len(array[i])):
            if skip != 0:
                skip -= 1
                continue
            if checkIfNumber(array, i, j):
                number, skip = getNumber(array, i, j, len(array[i]))
                if checkSurrounding(array, i, j, number):
                    result += number
    print(result)
