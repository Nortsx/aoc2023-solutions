import math

inputfile = open('input.txt','r')

map = []

# The whole trick is to go over the path and calculate the lenght. In my real example path lenght was around 12K elements, so recursive approach won't do.
# But it is not needed, since we are having only one way really

pipe_elements = {
    '.': [],
    '|': [[0, 1], [0, -1]],
    '-': [[-1, 0], [1, 0]],
    'L': [[0, -1], [1, 0]],
    'J': [[0, -1], [-1, 0]],
    '7': [[0, 1], [-1, 0]],
    'F': [[0, 1], [1, 0]],
    'S': [[0, 1], [0, -1], [-1, 0], [1, 0]]
}

for line in inputfile:
    map.append(line.strip())

start_coord = [0, 0]

for column_index, column in enumerate(map):
    for row_index, char in enumerate(column):
        if char == 'S':
            start_coord = [row_index, column_index]
            break


def get_point_exits(coord, map, incoming_direction) -> []:
    if coord[1] < 0 or coord[1] >= len(map):
        return []
    if coord[0] < 0 or coord[0] >= len(map[coord[1]]):
        return []

    possible_entries = pipe_elements[map[coord[1]][coord[0]]]
    exits = []
    for entry in possible_entries:
        if entry != incoming_direction:
            exits.append(entry)
    if len(possible_entries) == len(exits):
        return []
    else:
        return exits

entries = []
possible_starts = pipe_elements['S']
starting_points = []

for possible_start in possible_starts:
    incoming_direction = [-1 * possible_start[0], -1 * possible_start[1]]
    exits = get_point_exits([start_coord[0] + possible_start[0], start_coord[1] + possible_start[1]], map, incoming_direction)
    if exits:
        starting_points.append(exits)

path = [start_coord]
current_coord = [start_coord[0] + starting_points[0][0][0], start_coord[1] + starting_points[0][0][1]]
current_direction = [-1 * starting_points[0][0][0], -1 * starting_points[0][0][1]]

while True:
    if map[current_coord[1]][current_coord[0]] == 'S':
        break
    exits = get_point_exits(current_coord, map, current_direction)
    path.append(current_coord)
    current_coord = [current_coord[0] + exits[0][0], current_coord[1] + exits[0][1]]
    current_direction = [-1 * exits[0][0], -1 * exits[0][1]]

print(math.ceil(len(path) / 2.0))

