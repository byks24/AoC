import numpy as np


def checkIfNumber(arr, i, j):
    if arr[i][j].isdigit():
        return True
    else:
        return False


def checkIfGear(arr, i, j):
    if arr[i][j] == '*':
        return 1
    else:
        return 0


def getNumber(arr, i, j, arraySize):
    string = arr[i][j]
    jj = j
    while jj + 1 < arraySize and arr[i][jj + 1].isdigit():
        string = string + arr[i][jj + 1]
        jj += 1
    jj = j
    while jj - 1 >= 0 and arr[i][jj - 1].isdigit():
        string = arr[i][jj - 1] + string
        jj -= 1
    return int(string)


def checkSurrounding(arr, i, j):
    digits = 0
    numbers=[]
    for ii in range(i - 1, i + 2):
        buffer = 0
        for jj in range(j - 1, j + 2):
            if arr[ii][jj].isdigit():
                if buffer == 0:
                    numbers.append(getNumber(arr, ii, jj, len(arr[ii])))
                buffer = 1
            else:
                if buffer == 1:
                    buffer = 0
                    digits += 1
        if buffer == 1:
            digits += 1
    return digits, numbers


if __name__ == '__main__':
    result = 0
    array = np.genfromtxt("text.txt", dtype=str, comments="Comment")

    for i in range(array.size):
        for j in range(len(array[i])):
            isGear = checkIfGear(array, i, j)
            if isGear:
                digits, numbers = checkSurrounding(array, i, j)
                if digits==2:
                    result += numbers[0]*numbers[1]
    print(result)
