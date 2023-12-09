inputfile = open('input.txt','r')
result = 0
for sequence in inputfile:
    elements = sequence.split(' ')
    converted_elements = []
    for elem in elements:
        converted_elements.append(int(elem))
    subsequences = [converted_elements]
    current_sequence = elements
    while True:
        current_subsequence = []
        current_element = int(current_sequence[0])
        for i in range(1, len(current_sequence)):
            current_subsequence.append(int(current_sequence[i]) - current_element)
            current_element = int(current_sequence[i])

        found_last = True
        for elem in current_subsequence:
            if elem != 0:
                found_last = False
                break

        if found_last:
            break
        else:
            subsequences.append(current_subsequence)
            current_sequence = current_subsequence

    print(subsequences)
    next_element = 0
    for seq in reversed(subsequences):
        next_element = seq[-1] + next_element
    result += next_element

print(result)


