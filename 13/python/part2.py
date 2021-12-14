import sys

points = []
folds = []
got_all_points = False

for line in sys.stdin:
    if got_all_points:
        s, value = line.rstrip().split('=')
        folds.append((s[-1], int(value)))
    else:
        if line.rstrip() == '':
            got_all_points = True
        else:
            points.append(
                tuple(
                    map(
                        int,
                        line.rstrip().split(','),
                    ),
                ),
            )

def split_y(points, value):
    new_points = []
    for point in points:
        if point[1] < value:
            if point not in new_points:
                new_points.append(point)
        elif point[1] > value:
            x = point[0]
            y = value - (point[1] - value)
            if (x, y) not in new_points:
                new_points.append((x, y))
    return new_points

def split_x(points, value):
    new_points = []
    for point in points:
        if point[0] < value:
            if point not in new_points:
                new_points.append(point)
        elif point[0] > value:
            x = value - (point[0] - value)
            y = point[1]
            if (x, y) not in new_points:
                new_points.append((x, y))
    return new_points

for fold in folds:
    if fold[0] == 'y':
        points = split_y(points, fold[1])
    else:
        points = split_x(points, fold[1])
    print(points)

print(len(points))

canvas = []
for y in range(10):
    canvas.append(['.'] * 50)

for point in points:
    canvas[point[1]][point[0]] = '#'

for line in canvas:
    print(''.join(line))
