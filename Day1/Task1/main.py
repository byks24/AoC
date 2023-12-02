
result=0

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        for line in f:
            array = [None, None]
            for char in range(len(line)):
                if line[char].isdigit():
                    if array[0] is None:
                        array[0] = int(line[char])
                    else:
                        array[1] = int(line[char])
            if array[1] == None:
                array[1] = array[0]
            result+=array[0]*10+array[1]
        print(result)

