import re
regex = r"(Card\s+\d+):(.+)\|(.+)"
numbersRegex = r"\b\d+\b"

inputfile = open('input.txt','r')

total_score = 0

cards_owned = []

#pretty much the same idea, just score count is a tad different

for line in inputfile:
    cards_owned.append(1)

inputfile.seek(0)
for index, line in enumerate(inputfile):
    matches = re.findall(regex, line)
    print(line)
    print(matches)
    winningNumbers = re.findall(numbersRegex, matches[0][1])
    cardNumbers = re.findall(numbersRegex, matches[0][2])
    winningSet = set()
    for number in winningNumbers:
        winningSet.add(number)

    offset = index
    for number in cardNumbers:
        if number in winningSet:
            offset += 1
            cards_owned[offset] += cards_owned[index]

print(cards_owned)

for card in cards_owned:
    total_score += card

print(total_score)