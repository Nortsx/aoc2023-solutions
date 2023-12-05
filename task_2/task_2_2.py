import re
inputfile = open('input.txt','r')

regex = r"Game (\d+):(.+)"
gameregex = r"(\d+) (red|green|blue)"

games_sum = 0


def check_minimums(gamesets):
    cubes_needed = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game in gamesets:
        results = re.findall(gameregex, game.strip())
        for result in results:
            if cubes_needed[result[1]] < int(result[0]):
                cubes_needed[result[1]] = int(result[0])

    return cubes_needed["red"]*cubes_needed["green"]*cubes_needed["blue"]


for line in inputfile:
    matches = re.findall(regex, line)
    gameid = matches[0][0]
    games = matches[0][1].strip()
    print(gameid)
    game_sets = games.split(';')
    games_sum += check_minimums(game_sets)
    print(line)

print(games_sum)