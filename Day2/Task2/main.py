result=0
if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        for line in f:
            gameID = line.split(":")[0].split()[1]
            rounds = line.split(":")[1].split(";")
            red = 1
            green = 1
            blue = 1
            for i in range(len(rounds)):
                colours = rounds[i].split(",")
                for j in range(len(colours)):
                    if "red" in colours[j].split() and int(colours[j].split()[0]) > red:
                        red = int(colours[j].split()[0])
                    if "green" in colours[j].split() and int(colours[j].split()[0]) > green:
                        green = int(colours[j].split()[0])
                    if "blue" in colours[j].split() and int(colours[j].split()[0]) > blue:
                        blue = int(colours[j].split()[0])

            result += red*green*blue
        print("result:")
        print(result)

