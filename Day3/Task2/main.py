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


def getNumber(arr, i, j):
    string = arr[i][j]
    jj = j
    while jj + 1 < arr[i] and arr[i][jj + 1].isdigit(): # search for additional numbers on right
        string = string + arr[i][jj + 1]
        jj += 1
    jj = j
    while jj - 1 >= 0 and arr[i][jj - 1].isdigit(): # search for additional numbers on left
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
                if buffer == 0: # if it is 1st occurence of digit in a line find it and save in a list
                    numbers.append(getNumber(arr, ii, jj))
                buffer = 1
            else:
                if buffer == 1: # if found another char other than digit reset buffer and add to digit counter
                    buffer = 0
                    digits += 1
        if buffer == 1: # if digit is the last char in 3rd column of 3x3 array then add it to counter
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
