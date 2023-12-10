import numpy as np
from shapely.geometry import Polygon

pipe_symbols_moves = {
    "|": [((1, 0), (1, 0)), ((-1, 0), (-1, 0))],  # 1st tuple is previous move, 2nd is current move
    "-": [((0, 1), (0, 1)), ((0, -1), (0, -1))],
    "L": [((0, -1), (-1, 0)), ((1, 0), (0, 1))],
    "J": [((0, 1), (-1, 0)), ((1, 0), (0, -1))],
    "7": [((-1, 0), (0, -1)), ((0, 1), (1, 0))],
    "F": [((-1, 0), (0, 1)), ((0, -1), (1, 0))]
}

pipe_symbols_moves_dict = {
    "|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},  # 1st tuple is previous move, 2nd is current move
    "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "L": {(0, -1): (-1, 0), (1, 0): (0, 1)},
    "J": {(0, 1): (-1, 0), (1, 0): (0, -1)},
    "7": {(-1, 0): (0, -1), (0, 1): (1, 0)},
    "F": {(-1, 0): (0, 1), (0, -1): (1, 0)}
}

pipe_symbols_check = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(1, 0), (0, -1)],
    "J": [(0, -1), (1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(-1, 0), (0, -1)]
}

poly_corners = [
    "L",
    "J",
    "7",
    "F"
]


def read_input(filename):
    with open(filename) as f:
        ret = np.array(f.read().splitlines())
        arr = np.zeros((len(ret), len(ret[0])), dtype=str)
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                arr[i, j] = ret[i][j]
    return arr

tuples = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # over left right under
cords = {}
result = 0
arr = []
line = []
if __name__ == '__main__':
    file = read_input("text.txt")
    starting_points = []
    s1 = np.where(file == 'S')[0][0]  # x
    s2 = np.where(file == 'S')[1][0]  # y
    for i, j in tuples:
        if (file[s1 + i, s2 + j].item() in pipe_symbols_check) and (
                (i, j) in pipe_symbols_check[file[s1 + i, s2 + j].item()]):
            starting_points.append((i, j))
    cords[(s1, s2)] = 'S'
    line.append((s1, s2))
    counter = 0
    cordsx = s1
    cordsy = s2

    xx = s1
    yy = s2
    y = yy + starting_points[0][1]
    x = xx + starting_points[0][0]
    while file[x, y].item() != 'S':
        counter += 1
        tup = pipe_symbols_moves_dict[file[x, y].item()][(x - xx, y - yy)]
        cordsx += x - xx
        cordsy += y - yy
        line.append((x, y))
        xx = x
        yy = y
        x = x + tup[0]
        y = y + tup[1]

    p = Polygon(line)
    print("results: ")
    print(int(p.area) - len(line) / 2 + 1)  # calculate area of polygon and remove pipe area
