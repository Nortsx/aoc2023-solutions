import re
inputfile = open('input.txt','r')

constraints = {
    "red": 12,
    "green": 13,
    "blue": 14
}
regex = r"Game (\d+):(.+)"
gameregex = r"(\d+) (red|green|blue)"

games_sum = 0

# could be done with a single regex without any splits

def check_constraints(gamesets):
    for game in gamesets:
        results = re.findall(gameregex, game.strip())
        for result in results:
            if constraints[result[1]] < int(result[0]):
                return False
    return True


for line in inputfile:
    matches = re.findall(regex, line)
    gameid = matches[0][0]
    games = matches[0][1].strip()
    print(gameid)
    gamesets = games.split(';')
    print(gamesets)
    if check_constraints(gamesets):
        games_sum += int(gameid)
    print(line)

print(games_sum)
