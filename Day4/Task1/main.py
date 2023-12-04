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
            numbers=line.split(":")[1].split("|")
            winning_numbers = numbers[0].split()
            our_numbers=numbers[1].split()
            print("gameid"+ str(gameID))
            print(numbers)
            score=0
            for i in range(len(winning_numbers)):
                for j in range(len(our_numbers)):
                    if int(winning_numbers[i]) == int(our_numbers[j]):
                        print("wins "+winning_numbers[i] +" in our is " + our_numbers[j])

                        score+=1
            print("score "+str(score))

            if score !=0:
                print("adding result " + str(2 ** (score - 1)))
                result+=2**(score-1)
            print("mid result"+str(result))
        print("result:")
        print(result)
