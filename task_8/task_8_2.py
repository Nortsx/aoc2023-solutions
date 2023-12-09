import re

# The principle in short is to find amount of moves for each node and find LCM for all of them.

class TreeNode(object):
    def __init__(self, name: str):
        self.name = name
        self.left_node = None
        self.right_node = None

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def set_left_node(self, node: 'TreeNode'):
        self.left_node = node

    def set_right_node(self, node: 'TreeNode'):
        self.right_node = node


class DirectionsSource:
    def __init__(self, directions:[]):
      self.directions = directions

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        res = self.directions[self.index]
        self.index += 1
        if self.index >= len(self.directions):
            self.index = 0
        return res


nodes_regex = r"(\w{3}) = \((\w{3}), (\w{3})\)"

inputfile = open('input.txt','r')

directionsLine = inputfile.readline()
inputfile.readline()

print(directionsLine)
nodes_dict = {}
simultaneous_nodes = []
exit_moves = []
for nodeline in inputfile:
    matches = re.findall(nodes_regex, nodeline)
    print(matches)
    if matches[0][0] in nodes_dict:
        node = nodes_dict[matches[0][0]]
    else:
        node = TreeNode(matches[0][0])
        nodes_dict[matches[0][0]] = node
    if node.name[2] == 'A':
        simultaneous_nodes.append(node)
    if matches[0][0] != matches[0][1]:
        if matches[0][1] in nodes_dict:
            left_node = nodes_dict[matches[0][1]]
        else:
            left_node = TreeNode(matches[0][1])
            nodes_dict[matches[0][1]] = left_node
        node.set_left_node(left_node)

    if matches[0][0] != matches[0][2]:
        if matches[0][2] in nodes_dict:
            right_node = nodes_dict[matches[0][2]]
        else:
            right_node = TreeNode(matches[0][2])
            nodes_dict[matches[0][2]] = right_node
        node.set_right_node(right_node)


source = DirectionsSource(directionsLine.strip())
iterator = iter(source)


for node in simultaneous_nodes:
    tmp_node = node
    for index, item in enumerate(iterator):
        if item == 'L':
            tmp_node = tmp_node.get_left_node()
        if item == 'R':
            tmp_node = tmp_node.get_right_node()
        if tmp_node.name[2] == 'Z':
            exit_moves.append(index+1)
            break

max_move = 0
total_multiplication = 1
lcm = 0

for move in exit_moves:
    max_move = max(max_move, move)
    total_multiplication *= move


def find_lcm(num1, num2):
    for index in range(max(num1, num2), 1 + (num1 * num2), max(num1, num2)):
        if index % num1 == index % num2 == 0:
            return index


currentLCM = find_lcm(exit_moves[0],exit_moves[1])

for i in range(2, len(exit_moves)):
    currentLCM = find_lcm(currentLCM, exit_moves[i])

print(currentLCM)
