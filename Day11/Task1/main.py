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
if __name__ == '__main__':
    file = read_input("text.txt")
    for i in range(len(file)):

        index = 0

        line = file[i].replace("\n", "")
        shape = len(line)
        array = np.array(line, dtype=str)
        split_line = np.zeros(len(line), dtype=str)

        for j in range(len(line)):
            split_line[j] = line[j]

        galaxy = np.append(galaxy, split_line)

        if np.all(split_line == '.'):
            galaxy = np.append(galaxy, split_line)
    galaxy = np.reshape(galaxy, (-1, shape))
    for i in range(counter):
        second_range = counter - i - 1
        for j in range(second_range):
            combinations.append((i + 1, j + i + 2))
    new_galaxy = np.copy(galaxy).T
    counterrows = 0
    for row in range(galaxy.T.shape[0]):
        if np.all(galaxy.T[row] == '.'):
            new_galaxy = np.insert(new_galaxy, row + counterrows, ['.'], axis=0)
            counterrows += 1
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

            result += (abs(stars[str(int(j + i + 2))][0] - stars[str(int(i + 1))][0]) + abs(
                stars[str(int(j + i + 2))][1] - stars[str(int(i + 1))][1]))
    print(result)

