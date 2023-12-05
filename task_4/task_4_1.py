import re
regex = r"(Card\s+\d+):(.+)\|(.+)"
numbersRegex = r"\b\d+\b"

inputfile = open('input.txt','r')

# again, you can easily combine to regex, for me it is just easier to follow this way.

total_score = 0
for line in inputfile:
    cardScore = 0
    matches = re.findall(regex, line)
    print(line)
    print(matches)
    winningNumbers = re.findall(numbersRegex, matches[0][1])
    cardNumbers = re.findall(numbersRegex, matches[0][2])
    winningSet = set()
    for number in winningNumbers:
        winningSet.add(number)

    for number in cardNumbers:
        if number in winningSet:
            cardScore = 1 if cardScore == 0 else cardScore << 1

    total_score += cardScore


print(total_score)
