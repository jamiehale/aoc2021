import sys
from functools import reduce

def height_at(x, y, heights):
    return heights[y][x]

def add_to_basin_at(x, y, heights, set):
    if (x, y) in set:
        return
    print(f'Adding {x},{y} to {set}')
    set.append((x, y))
    height = height_at(x, y, heights)
    if y > 0:
        if (x, y - 1) not in set:
            up_height = height_at(x, y - 1, heights)
            if up_height != 9 and up_height > height:
                add_to_basin_at(x, y - 1, heights, set)
    if y < (len(heights) - 1):
        if (x, y + 1) not in set:
            down_height = height_at(x, y + 1, heights)
            if down_height != 9 and down_height > height:
                add_to_basin_at(x, y + 1, heights, set)
    if x > 0:
        if (x - 1, y) not in set:
            left_height = height_at(x - 1, y, heights)
            if left_height != 9 and left_height > height:
                add_to_basin_at(x - 1, y, heights, set)
    if x < (len(heights[0]) - 1):
        if (x + 1, y) not in set:
            right_height = height_at(x + 1, y, heights)
            if right_height != 9 and right_height > height:
                add_to_basin_at(x + 1, y, heights, set)
        
def get_basin_size(x, y, heights):
    print(f'Starting a basin at {x},{y}')
    set = []
    add_to_basin_at(x, y, heights, set)
    return len(set)
    
heights = []
for line in sys.stdin:
    these_heights = list(
        map(
            int,
            list(line.rstrip())
        )
    )
    heights.append(these_heights)

basin_sizes = []
for y, line in enumerate(heights):
    is_first_line = y == 0
    is_last_line = y == (len(heights) - 1)
    for x, height in enumerate(line):
        is_first_column = x == 0
        is_last_column = x == (len(line) - 1)
        surrounding_heights = []
        if not is_first_line:
            surrounding_heights.append(height_at(x, y - 1, heights))
        if not is_last_line:
            surrounding_heights.append(height_at(x, y + 1, heights))
        if not is_first_column:
            surrounding_heights.append(height_at(x - 1, y, heights))
        if not is_last_column:
            surrounding_heights.append(height_at(x + 1, y, heights))
        lowest = True
        for h in surrounding_heights:
            if height >= h:
                lowest = False
                break
        if lowest:
            basin_sizes.append(get_basin_size(x, y, heights))

print(reduce(lambda a, b: a * b, list(reversed(sorted(basin_sizes)))[0:3]))
