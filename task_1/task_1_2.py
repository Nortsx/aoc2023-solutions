input = open('input.txt', 'r')

# using regular expression with lookaround is possible here but quite complicated as an approach, so I decided for some loops here


def check_char_in_number(number_substring):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, number in enumerate(numbers):
        if len(number_substring) > len(number):
            continue
        else:
            if number_substring == number[0:len(number_substring)]:
                if len(number_substring) == len(number):
                    return index
                else:
                    return 10  # we have to see if match is there
    return -1


def convert_string_values_to_numbers(line):
    resulting = ''
    char_count = 0
    count_position = 0
    included_elements = 1
    while char_count < len(line):
        char = line[char_count]
        if char.isalpha():
            # print(char)
            checkResult = check_char_in_number(line[count_position:count_position + included_elements])
            if checkResult == -1:
                char_count = count_position
                count_position += 1
                included_elements = 1
            elif checkResult == 10:
                included_elements += 1
            else:
                resulting += str(checkResult)
                char_count = count_position
                count_position += 1
        else:
            resulting += char
            count_position = char_count + 1
            included_elements = 1
        char_count += 1
    return resulting


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
    sum += read_number_from_line(convert_string_values_to_numbers(line))
print(sum)
