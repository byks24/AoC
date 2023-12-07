zero = {}
one_pair = {}
two_pairs = {}
house = {}
three = {}
four = {}
five = {}
pokerCardValues = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}


def sort(dict1, values):
    tmp = {}
    for i in dict1:
        sum = 0
        for j in range(5):
            string = str(i)
            sum += 10 ** ((5 - j) * 2) * int(values[string[j]])
        tmp[i] = sum
    sorted_tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict()

    for cards, score in sorted_tmp:
        sorted_dict.setdefault(cards, []).append(dict1[cards])
    return sorted_dict


def read_input(filename):
    with open(filename) as f:
        ret = f.readlines()
    return ret


if __name__ == '__main__':
    file = read_input("text.txt")
    for i in range(len(file)):
        line = file[i].split()
        bid = line[1]
        sorted_line = sorted(line[0])
        reps1 = 0
        reps2 = 0
        end_of_rep1 = 0
        jokers = 0
        if (sorted_line[0] == "J"):
            jokers += 1
        for j in range(1, 5):
            if (sorted_line[j] == "J"):
                jokers += 1
            elif (sorted_line[j] == sorted_line[j - 1]) and end_of_rep1 == 0 and sorted_line[j] != "J":
                if reps1 == 0:
                    reps1 = 2
                else:
                    reps1 += 1
            elif (sorted_line[j] == sorted_line[j - 1]) and end_of_rep1 == 1 and sorted_line[j] != "J":
                if reps2 == 0:
                    reps2 = 2
                else:
                    reps2 += 1
            elif (sorted_line[j] != sorted_line[j - 1]) and reps1 > 0 and sorted_line[j] != "J":
                end_of_rep1 = 1
        if reps1 == 0 and reps2 == 0:
            if jokers >= 1 and jokers < 5:
                reps1 = reps1 + jokers + 1
            else:
                reps1 = reps1 + jokers
        elif reps1 > reps2:
            reps1 = reps1 + jokers
        else:
            reps2 = reps2 + jokers
        if reps1 == 0 and reps2 == 0:
            zero[str(line[0])] = int(bid)
        elif (reps1 == 2 and reps2 == 3) or (reps1 == 3 and reps2 == 2):
            house[str(line[0])] = int(bid)
        elif reps1 == 2 and reps2 == 2:
            two_pairs[str(line[0])] = int(bid)
        elif reps1 == 2 or reps2 == 2:
            one_pair[str(line[0])] = int(bid)
        elif reps1 == 3 or reps2 == 3:
            three[str(line[0])] = int(bid)
        elif reps1 == 4 or reps2 == 4:
            four[str(line[0])] = int(bid)
        elif reps1 == 5 or reps2 == 5:
            five[str(line[0])] = int(bid)
    sorted_zero = sort(zero, pokerCardValues)
    sorted_one = sort(one_pair, pokerCardValues)
    sorted_two = sort(two_pairs, pokerCardValues)
    sorted_three = sort(three, pokerCardValues)
    sorted_four = sort(four, pokerCardValues)
    sorted_five = sort(five, pokerCardValues)
    sorted_house = sort(house, pokerCardValues)
    merged = {**sorted_five, **sorted_four, **sorted_house, **sorted_three, **sorted_two, **sorted_one, **sorted_zero}
    result = 0
    i = 0
    for key in merged:
        result += merged[key][0] * (len(merged) - i)
        i += 1
    print(result)
