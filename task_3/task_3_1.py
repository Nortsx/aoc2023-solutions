symbols = {'$','*','#','+','@','/','-','&','=','%'}

# basic logic here is to parse complete number and find a square around it to analyse for any symbols that are marking it as
# a part. The trick tho is to add last . to the loop because otherwise last number in line won't be analysed

def find_the_symbol(lines):
    for line in lines:
        if len(line) > 0:
            for character in line:
                if character in symbols:
                    return True
    return False


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

    return lines_to_analyse

with open('input.txt') as file:
    partsmap = [line.rstrip() for line in file]
    lines_sum = 0
    for lineIndex, symbolsline in enumerate(partsmap):
        print(lineIndex)
        print(symbolsline)
        startPosition = -1
        for charIndex, character in enumerate(symbolsline+"."):
            if character.isdigit():
                if startPosition == -1:
                    startPosition = charIndex
            elif character == '.' or character in symbols:
                if startPosition > -1:
                    print(generate_search_lines(startPosition, lineIndex, charIndex, partsmap))
                    if find_the_symbol(generate_search_lines(startPosition, lineIndex, charIndex, partsmap)):
                        lines_sum += int(symbolsline[startPosition:charIndex])
                    startPosition = -1



    print(lines_sum)

