locations = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 1\locations.txt", "r")

left = []
right = []

for line in locations:
    line = line.split("   ")
    left.append(int(line[0]))
    right.append(int(line[1].strip()))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    diff = abs(left[i] - right[i])
    total += diff

print(total)



