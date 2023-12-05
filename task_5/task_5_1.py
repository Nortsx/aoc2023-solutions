import re
file = open('input.txt', 'r')

seeds_regex = r"seeds:\s*(\d+(?:\s+\d+)*)"
seeds_line = file.readline()
matches = re.findall(seeds_regex, seeds_line)
seeds = matches[0].split(' ')
file.readline()


def get_transformation_dictionary_from_file(file):
    transformation_dict = {}

    current_dictionary_key = ""
    for line in file:
        if len(line) > 1:
            if line[0].isalpha():
                name = line.replace(" map:\n", "")
                transformation_dict[name] = []
                current_dictionary_key = name
            else:
                numbers = line.split(' ')
                print(numbers)
                transformation_dict[current_dictionary_key].append({"source": int(numbers[1]), "dest": int(numbers[0]), "interval": int(numbers[2])})
    return transformation_dict


def find_location_for_seed(transformation_dict, seed_value):
    current_transformation = "seed"
    current_value = seed_value
    while current_transformation != "location":
        for transform in transformation_dict:
            directions = transform.split("-to-")
            if current_transformation == directions[0]:
                current_transformation = directions[1]
                for interval in transformation_dict[transform]:
                    if interval['source'] <= current_value < interval["source"] + interval["interval"]:
                        current_value = interval['dest'] + (current_value - interval["source"])
                        break
                # print(current_transformation)
                # print(current_value)
    return current_value


transformation_dict = get_transformation_dictionary_from_file(file)
seed_min = find_location_for_seed(transformation_dict, int(seeds[1]))

for seed in seeds:
    location = find_location_for_seed(transformation_dict, int(seed))
    print(seed)
    print(location)
    if location < seed_min:
        seed_min = location

print(seed_min)