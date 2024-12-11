import re

memory = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 3\memory.txt", "r")

mem_string = memory.read()

pattern = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"

record = True
results = []

for match in re.finditer(pattern, mem_string):
    if match.group(1):
        record=True
    elif match.group(2):
        record=False
    elif match.group(3) and record:
        X = int(match.group(4))
        Y = int(match.group(5))
        results.append((X,Y))
    
total = 0

for mul in results:
    total += (mul[0] * mul[1])

print(total)