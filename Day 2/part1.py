results = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 2\data.txt", "r")

total_safe = 0

def isSafe(line: list) -> int:
    ascending = True
    safe = True

    if line[0] > line[1]:
        ascending = False

    for i in range(len(line) - 1):
        current_val = line[i]
        next_val = line[i+1]
        if ascending:
            if (current_val < next_val) and ((abs(current_val - next_val) > 0) and (abs(current_val - next_val) < 4)):
                pass
            else:
                safe = False
        else:
            if (current_val > next_val) and ((abs(current_val - next_val) > 0) and (abs(current_val - next_val) < 4)):
                pass
            else:
                safe = False
    
    if safe:
        return 1
    else:
        return 0

for line in results:
    total_safe += isSafe(list(map(int, line.split(" "))))

print(total_safe)