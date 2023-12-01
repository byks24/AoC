# This is a sample Python script.
import  numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


result=0

# Press the green button in the gutter to run the script.
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
