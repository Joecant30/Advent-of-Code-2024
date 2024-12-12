import math

puzzle = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 4\puzzle.txt", "r")

puzzle_grid = [line.strip() for line in puzzle]

word = "MAS"

X1 = [1,1]
X2 = [1,-1]

rows = len(puzzle_grid)
cols = len(puzzle_grid[0]) if rows > 0 else 0

def find_word_in_grid(grid, word):

    total_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[math.floor(len(word)/2)]:
                if (check_direction(grid, r-1, c-1, word, X1[0], X1[1]) or check_direction(grid, r-1, c-1, word[::-1], X1[0], X1[1])) and (check_direction(grid, r-1, c+1, word, X2[0], X2[1]) or check_direction(grid, r-1, c+1, word[::-1], X2[0], X2[1])):
                    total_count += 1

    return total_count

def check_direction(grid, start_row, start_col, word, dx, dy):
    print(word)
    for i in range(len(word)):
        nr = start_row + i * dx
        nc = start_col + i * dy
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
            return False
    return True

print(find_word_in_grid(puzzle_grid, word))