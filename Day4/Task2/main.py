result = 0
fail = 0
games = [0]
if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        for line in f:

            gameID = line.split(":")[0].split()[1]
            numbers = line.split(":")[1].split("|")
            winning_numbers = numbers[0].split()
            our_numbers = numbers[1].split()

            round_result = 0
            if len(games) < int(gameID):
                games.append(int(0))
            games[int(gameID) - 1] += 1
            score = 0
            for i in range(len(winning_numbers)):

                for j in range(len(our_numbers)):
                    if int(winning_numbers[i]) == int(our_numbers[j]):
                        score += 1
            if score != 0:
                retries = games[int(gameID) - 1]
                for won in range(score):
                    if (len(games)) < score + int(gameID):
                        games.append(0)
                    games[int(gameID) + int(won)] += int(1 * retries)
        for i in range(len(games)):
            result += games[i]
        print("result:")
        print(result)
