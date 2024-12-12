puzzle = open("C:\Repo\Advent of Code 2024\Advent-of-Code-2024\Day 4\puzzle.txt", "r")

puzzle_grid = [line.strip() for line in puzzle]

word = "XMAS"

directions = [
        (0, 1),   # Horizontal left-to-right
        (0, -1),  # Horizontal right-to-left
        (1, 0),   # Vertical top-to-bottom
        (-1, 0),  # Vertical bottom-to-top
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

rows = len(puzzle_grid)
cols = len(puzzle_grid[0]) if rows > 0 else 0

def find_word_in_grid(grid, word):

    total_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                for dx, dy in directions:
                    if check_direction(grid, r, c, word, dx, dy):
                        total_count += 1

    return total_count

def check_direction(grid, start_row, start_col, word, dx, dy):

    for i in range(len(word)):
        nr = start_row + i * dx
        nc = start_col + i * dy
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
            return False
    return True

print(find_word_in_grid(puzzle_grid, word))