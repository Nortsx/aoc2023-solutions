import re

# I do suspect it is possible to solve this problem with a formula, by plotting two graphs and finding a function describing their intersection. But as we are in programming world, let's get going with programmatic approach

inputfile = open('input.txt','r')

timeline = inputfile.readline()
distanceline = inputfile.readline()

times = re.findall(r'\d+', timeline.split(":")[1])
distances = re.findall(r'\d+', distanceline.split(":")[1])


result = 1

for index, time_string in enumerate(times):
    distance = int(distances[index])
    time = int(time_string)
    chargeTime = 1
    triesPossible = 0

    # chargin for the whole time of race doesn't make sense
    while chargeTime < int(time):
        if chargeTime * (time - chargeTime) > distance:
            triesPossible += 1
        chargeTime += 1

    result *= triesPossible

print(result)