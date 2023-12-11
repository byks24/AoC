import numpy as np


def read_input(filename):
    with open(filename) as f:
        ret = f.readlines()
    return ret

result = 0
galaxy = np.empty(shape=(0, 0))
stars = {}
combinations = []
counter = 0
gapsX = []
gapsY = []
if __name__ == '__main__':
    file = read_input("text.txt")
    for i in range(len(file)):

        index = 0

        line = file[i].replace("\n", "")
        shape = len(line)
        array = np.array(line, dtype=str)
        split_line = np.zeros(len(line), dtype=str)
        dots_counter = 0
        for j in range(len(line)):
            dots_counter = 0
            for dots in range(len(line)):
                if line[dots] == '.':
                    dots_counter += 1
            if dots_counter == len(line):
                split_line[j] = '+'
            else:
                split_line[j] = line[j]
        if dots_counter == len(line):
            gapsX.append(i)

        galaxy = np.append(galaxy, split_line)
    galaxy = np.reshape(galaxy, (-1, shape))
    for i in range(counter):
        second_range = counter - i - 1
        for j in range(second_range):
            combinations.append((i + 1, j + i + 2))
    new_galaxy = np.copy(galaxy).T
    counterrows = 0
    for row in range(galaxy.T.shape[0]):
        counter1 = 0
        for i in range(galaxy.T.shape[1]):
            if galaxy.T[row][i] == "." or galaxy.T[row][i] == "+":
                counter1 += 1

        if (counter1 == galaxy.T.shape[1]):
            gapsY.append(row)
            for i in range(galaxy.T.shape[1]):
                new_galaxy[row][i] = '+'
    galaxy = new_galaxy.T
    for i in range(galaxy.shape[0]):
        for j in range(galaxy.shape[1]):
            if galaxy[i][j] == "#":
                counter += 1
                stars[str(counter)] = (i, j)

    for i in range(counter):
        second_range = counter - i - 1
        for j in range(second_range):
            combinations.append((i + 1, j + i + 2))
            stars1X = stars[str(int(i + 1))][0]
            stars1Y = stars[str(int(i + 1))][1]
            stars2X = stars[str(int(j + i + 2))][0]
            stars2Y = stars[str(int(j + i + 2))][1]
            result += (abs(stars[str(int(j + i + 2))][0] - stars[str(int(i + 1))][0]) + abs(
                stars[str(int(j + i + 2))][1] - stars[str(int(i + 1))][1]))
            for x in gapsX:
                if ((stars1X > x > stars2X) or (stars1X < x < stars2X)):
                    result += 999999
            for y in gapsY:
                if ((stars1Y > y > stars2Y) or (stars1Y < y < stars2Y)):
                    result += 999999

    print(result)
