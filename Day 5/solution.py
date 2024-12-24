from collections import defaultdict

file = open(r"C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 5\updates.txt", "r")

reachedUpdates = False

before = defaultdict(set)
after = defaultdict(set)

total = 0
total_mismatch = 0

for line in file:
    if not reachedUpdates:
        if len(line.strip()) == 0:
            reachedUpdates = True
        else:
            x,y = map(int, line.split("|"))
            before[y].add(x)
            after[x].add(y)
    else:
        line = list(map(int, line.split(",")))
        isValid = True
        for i, x in enumerate(line):
            for j, y in enumerate(line):
                if i < j and y in before[x]:
                    isValid = False
                    break

        if isValid:
            total += line[len(line)//2]
        else:
            n = len(line)
            for i in range(n-1):
                for j in range(n-1):
                    if line[j] not in before[line[j+1]]:
                        line[j], line[j+1] = line[j+1], line[j]
                        continue
            total_mismatch += line[len(line)//2] 


print(total)
print(total_mismatch)