import sys

def height_at(x, y, heights):
    return heights[y][x]

def add_to_basin_at(x, y, heights, set):
    if (x, y) in set:
        return
    set.append((x, y))
    height = height_at(x, y, heights)
    if y > 0:
        if height_at(x, y - 1, heights) > height:
            add_to_basin_at(x, y - 1, heights)
    if y == (len(heights) - 1):
        if height_at(x, y + 1, heights) > height:
            add_to_basin_at(x, y + 1, heights)
    if x == 0:
        if height_at(x - 1, y, heights) > height:
            add_to_basin_at(x - 1, y, heights)
    if x == (len(heights[0]) - 1):
        if height_at(x + 1, y, heights) > height:
            add_to_basin_at(x + 1, y, heights)
        
def get_basin_size(x, y, heights):
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

print(basin_sizes)
