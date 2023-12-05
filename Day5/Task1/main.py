import numpy as np

result = 0
index = 0
array=[]
if __name__ == '__main__':
        with open('test.txt', 'r') as f:
            for line in f:
                if "seeds: " in line:
                    string_seeds = line.split(" ", 1)[1].split()
                    seeds = [int(string) for string in string_seeds]
                    flags=np.zeros(len(seeds), dtype=int)
                    results = seeds
                elif line in ['\n', '\r\n']:
                    flags=np.zeros(len(seeds), dtype=int)
                elif "-" in line:
                    continue
                else:
                    for i in range(len(seeds)):
                        if flags[i] == 0 and int(line.split()[1]) <= seeds[i] <= (int(line.split()[1]) + int(line.split()[2])):
                            print(seeds[i])
                            print(int(line.split()[0]))
                            seeds[i]=int(line.split()[0])+seeds[i]-int(line.split()[1])
                            flags[i]=1
                    print(seeds)
        seeds.sort()
        print(seeds[0])