import re
import portion as I


# the whole problem here is that honest bruteforce is too long to calculate.
# But we can use the fact that each mapping is mapping an interval and we just have to find intersections using the same rules.
# Say you have seeds [0:100) and soils [10:20)->[50:60) [30:100)->[100:170)
# this way after mapping soild you are getting intervals [0:10) [50:60) [20:30) and [100:170) all of which you can analyse further in further transformation steps.
# At the end you get intervals of location and you actually need the lowest border from each interval. For this task I used interval library to get intersections and differences for brevity

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


def find_location_for_seed(transformation_dict, seed_interval):
    current_transformation = "seed"
    intervals_array = [seed_interval]
    print(seed_interval)
    while current_transformation != "location":
        for transform in transformation_dict:
            directions = transform.split("-to-")
            if current_transformation == directions[0]:
                current_transformation = directions[1]
                transformed_intervals = []
                while len(intervals_array) > 0:
                    interval_leftover = intervals_array.pop()
                    for interval in transformation_dict[transform]:
                        comparison_interval = I.closedopen(interval['source'], interval['source'] + interval['interval'])
                        intersection = interval_leftover & comparison_interval
                        if not intersection.empty:
                            diff = interval_leftover - intersection
                            if not diff.empty:
                                for leftover in diff:
                                    intervals_array.append(leftover)
                            transformed_intervals.append(I.closedopen(interval['dest'] + (intersection.lower - interval['source']),interval['dest'] + (intersection.upper - interval['source'])))
                            interval_leftover = None
                            break
                    if interval_leftover is not None:
                        transformed_intervals.append(interval_leftover)
                intervals_array = transformed_intervals
    min_result = intervals_array[0].lower
    for interval in intervals_array:
        if min_result > interval.lower:
            min_result = interval.lower
    return min_result


file = open('input.txt', 'r')

seeds_regex = r"seeds:\s*(\d+(?:\s+\d+)*)"
seeds_line = file.readline()
matches = re.findall(seeds_regex, seeds_line)
seeds_readings = matches[0].split(' ')
file.readline()
seeds = []

index = 0

while index < len(seeds_readings):
    seeds.append(I.closedopen(int(seeds_readings[index]), int(seeds_readings[index]) + int(seeds_readings[index+1])))
    index += 2


transformation_dict = get_transformation_dictionary_from_file(file)
seed_min = find_location_for_seed(transformation_dict, seeds[0])

for seed in seeds:
    location = find_location_for_seed(transformation_dict, seed)
    if location < seed_min:
        seed_min = location

print("$$$$$$$$$$$$$$$$$$$$$$")
print(seed_min)