result=0
max={
    "red":12,
    "green":13,
    "blue":14
}
fail=0
if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        for line in f:
            gameID=line.split(":")[0].split()[1]
            rounds=line.split(":")[1].split(";")
            fail = 0
            for i in range(len(rounds)):
                colours=rounds[i].split(",")
                for j in range(len(colours)):
                    if "red" in colours[j].split():
                        if int(colours[j].split()[0]) > int(max["red"]):
                            fail=1
                    if "green" in colours[j].split():
                        if int(colours[j].split()[0]) > int(max["green"]):
                            fail=1
                    if "blue" in colours[j].split():
                        if int(colours[j].split()[0]) > int(max["blue"]):
                            fail=1
            if fail == 0:
                result+=int(gameID)
        print("result:")
        print(result)

