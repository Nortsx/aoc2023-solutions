inputfile = open('input.txt','r')
result = 0

# This is the same as the old task, but with alteration of subtracting previous element, so literally the same code is reused

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
    prev_element = 0
    for seq in reversed(subsequences):
        prev_element = seq[0] - prev_element
    result += prev_element

print(result)


