import re

memory = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 3\memory.txt", "r")

mem_string = memory.read()

mul_list = re.findall("mul\((\d+),(\d+)\)", mem_string)

total = 0

for mul in mul_list:
    result = int(mul[0]) * int(mul[1])
    total += result

print(total)

