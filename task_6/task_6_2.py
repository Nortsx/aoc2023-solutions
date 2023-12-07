inputfile = open('input.txt','r')

timeline = inputfile.readline()
distanceline = inputfile.readline()

time = int(timeline.split(":")[1].replace(" ",""))
distance = int(distanceline.split(":")[1].replace(" ",""))

print(time)
print(distance)

# with much bigger input we prolly have to use binary search to reduce O(n) to O(log n)
# which is much faster considering we are dealing with billions now

result = 0

left = 1
right = time - 1

maxValidTime = 0
while left < right:
    mid = (right + left) // 2
    if mid*(time-mid) > distance:
        maxValidTime = mid
        left = mid + 1
    else:
        right = mid - 1


minValidTime = 0
left = 1
right = time - 1
while left < right:
    mid = (right + left) // 2
    if mid*(time-mid) > distance:
        minValidTime = mid
        right = mid - 1
    else:
        left = mid + 1

print(maxValidTime)
print(minValidTime)

print(maxValidTime - minValidTime + 1)