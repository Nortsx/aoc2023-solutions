
# here we are quite straightforward adding new elements to the universes and just iterating over an array

def check_empty(space: str) -> bool:
    for char in space:
        if char != '.':
            return False
    return True

file = open('input.txt','r')
galaxies = []

for line in file:
    galaxies.append(line.strip())
    if check_empty(line.strip()):
        galaxies.append(line.strip())

vertical_empty_spaces = []
for row, content in enumerate(galaxies[0]):
    row_list = []
    for line in galaxies:
        row_list.append(line[row])
    if check_empty("".join(row_list)):
        vertical_empty_spaces.append(row)

for index, row in enumerate(vertical_empty_spaces):
    for line_index, line in enumerate(galaxies):
        galaxies[line_index] = line[:row + index] + '.' + line[row+index:] #adding new vertical lines

galaxies_coords = []

for coord_y in range(len(galaxies)):
    for coord_x in range(len(galaxies[coord_y])):
        if galaxies[coord_y][coord_x] == "#":
            galaxies_coords.append([coord_x, coord_y])

pairs = []
for index_first, galaxy_a_coord in enumerate(galaxies_coords):
    for index_second in range(index_first+1, len(galaxies_coords)):
        pairs.append((galaxy_a_coord, galaxies_coords[index_second]))

print(len(pairs))

sum_pairs = 0

for pair in pairs:
    print(pair)
    sum_pairs += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

print(sum_pairs)