symbols = {'*'}

# the trick here was to reuse the code for 3.1 as much as possible.
# I bet more efficient algorithm would be to find all gears and analyse area around each one to look for any adjacent numbers,
# but as I had almost all the code I just modified this a bit

def generate_gears_map(partsmap):
    gears_map = {}
    for row, line in enumerate(partsmap):
        for column, char in enumerate(line):
            if char == '*':
                gears_map[str(row)+":"+str(column)] = []

    return gears_map


def find_the_symbol(lines, number, leftColumn, topRow, gearsMap):
    for line in lines:
        if len(line) > 0:
            for index, character in enumerate(line):
                if character in symbols:
                    gearsMap[str(topRow)+":"+str(leftColumn + index)].append(number)
        topRow += 1


def generate_search_lines(start_position, line_index, char_index, parts_map):
    middle_line = parts_map[line_index]
    top_line = line_index - 1
    bottom_line = line_index + 1
    start_column = start_position - 1
    end_column = char_index + 1
    lines_to_analyse = []

    if start_column < 0:
        start_column = 0
    if end_column >= len(middle_line):
        end_column = len(middle_line) - 1

    if top_line < 0:
        lines_to_analyse.append('')
    else:
        lines_to_analyse.append(parts_map[top_line][start_column:end_column])

    lines_to_analyse.append(middle_line[start_column:end_column])

    if bottom_line >= len(parts_map):
        lines_to_analyse.append('')
    else:
        lines_to_analyse.append(parts_map[bottom_line][start_column:end_column])

    return lines_to_analyse, start_column, top_line

with open('input.txt') as file:
    partsmap = [line.rstrip() for line in file]
    gearsmap = generate_gears_map(partsmap)
    lines_sum = 0
    for lineIndex, symbolsline in enumerate(partsmap):
        print(lineIndex)
        print(symbolsline)
        startPosition = -1
        for charIndex, character in enumerate(symbolsline+"."):
            if character.isdigit():
                if startPosition == -1:
                    startPosition = charIndex
            else:
                if startPosition > -1:
                    lines, start_x, top_y = generate_search_lines(startPosition, lineIndex, charIndex, partsmap)
                    find_the_symbol(lines,int(symbolsline[startPosition:charIndex]),start_x, top_y,gearsmap)
                    startPosition = -1

        print(gearsmap)

    for key in gearsmap:
        if len(gearsmap[key]) == 2:
            lines_sum += gearsmap[key][0]*gearsmap[key][1]

    print(lines_sum)

