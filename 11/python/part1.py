import sys

def print_grid(grid):
    for line in grid:
        print(''.join(map(str, line)))

def tick_line(line):
    return list(
        map(
            lambda x: x + 1,
            line,
        ),
    )

def tick(grid):
    return list(
        map(
            tick_line,
            grid,
        ),
    )

def get_new_flashes(grid, flash_set):
    flashes = []
    for y in range(len(grid)):
        values = grid[y]
        for x in range(len(values)):
            if values[x] > 9 and (x, y) not in flash_set:
                flashes.append((x, y))
    return flashes

def increment_at(x, y, grid):
    if x >= 0 and x < len(grid[0]):
        if y >= 0 and y < len(grid):
            grid[y][x] += 1

def flash_neighbours(grid, flashes):
    for (x, y) in flashes:
        for x1 in range(3):
            for y1 in range(3):
                if not (x1 == 1 and y1 == 1):
                    increment_at(x - 1 + x1, y - 1 + y1, grid)

def normalize_line(line):
    return list(
        map(
            lambda x: 0 if x > 9 else x,
            line,
        ),
    )

def normalize(grid):
    return list(
        map(
            normalize_line,
            grid,
        ),
    )

grid = []
for line in sys.stdin:
    grid.append(
        list(
            map(
                int,
                line.rstrip(),
            ),
        ),
    )

print('Before any steps:')
print_grid(grid)

total_flashes = 0

for i in range(100):
    grid = tick(grid)
    flash_set = []
    new_flashes = get_new_flashes(grid, flash_set)
    while len(new_flashes) > 0:
        flash_neighbours(grid, new_flashes)
        flash_set += new_flashes
        new_flashes = get_new_flashes(grid, flash_set)
    grid = normalize(grid)
    print(f'After step {i + 1}:')
    print_grid(grid)
    print(sorted(flash_set))
    total_flashes += len(flash_set)

print(total_flashes)
