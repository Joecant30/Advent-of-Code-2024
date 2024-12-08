locations = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 1\locations.txt", "r")

left = []
right = []

for line in locations:
    line = line.split("   ")
    left.append(int(line[0]))
    right.append(int(line[1].strip()))

unique_left = set(left)
dict_right = {}

for val in unique_left:
    dict_right[val] = right.count(val)

total = 0

for val in unique_left:
    total += left.count(val) * val * dict_right[val]

print(total)