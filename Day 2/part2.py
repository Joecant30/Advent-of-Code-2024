from part1 import isSafe

results = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 2\data.txt", "r")

total_safe = 0

for line in results:
    line = list(map(int, line.split(" ")))
    if isSafe(line) == 1:
        total_safe += 1
        pass
    else:
        for i in range(len(line)):
            temp = line.copy()
            temp.pop(i)
            if isSafe(temp) == 1:
                total_safe += 1
                break
    
print(total_safe)