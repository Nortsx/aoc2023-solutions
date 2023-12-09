import re

# It is yet another task with obvious logic of completion. Just build a tree, follow instructions and voila!
# For this particular task I felt myself a bit fancy so wrote a custom iterator.
# Normal while loop is not anywhere worse!

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
for nodeline in inputfile:
    matches = re.findall(nodes_regex, nodeline)
    print(matches)
    if matches[0][0] in nodes_dict:
        node = nodes_dict[matches[0][0]]
    else:
        node = TreeNode(matches[0][0])
        nodes_dict[matches[0][0]] = node
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

node = nodes_dict['AAA']
for index, item in enumerate(iterator):
    if item == 'L':
        node = node.get_left_node()
    if item == 'R':
        node = node.get_right_node()
    if node.name == 'ZZZ':
        print(index+1)
        break