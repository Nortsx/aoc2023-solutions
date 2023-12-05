input = open('input.txt', 'r')

# using two pointers could let us win some loops, but code is more readable this way IMO.

def read_number_from_line(line):
    charlist = []
    for char in line:
        if char.isnumeric():
            if len(charlist) == 0 or len(charlist) == 1:
                charlist.append(char)
            else:
                charlist[1] = char
    if len(charlist) == 1:
        charlist.append(charlist[0])
    return int(charlist[0]) * 10 + int(charlist[1])


sum = 0
for line in input:
    sum += read_number_from_line(line)
print(sum)
