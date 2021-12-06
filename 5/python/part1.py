import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'{self.x},{self.y}'


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def is_diagonal(self):
        if self.p1.x == self.p2.x:
            return False
        if self.p1.y == self.p2.y:
            return False
        return True
    
    def is_horizontal(self):
        return self.p1.y == self.p2.y

    def __repr__(self) -> str:
        return f'{self.p1} -> {self.p2}'


class Map:
    def __init__(self):
        self.heights = {}

    def _increment_height(self, x, y):
        row = self.heights.get(y)
        if row:
            row[x] = row.get(x, 0) + 1
        else:
            self.heights[y] = { x: 1 }

    def _draw_horizontal(self, x1, x2, y):
        print(f'Drawing horizontal line {x1},{y} -> {x2},{y}')
        start, end = list(sorted([x1, x2]))
        for x in range(start, end + 1):
            self._increment_height(x, y)

    def _draw_vertical(self, x, y1, y2):
        print(f'Drawing vertial line {x},{y1} -> {x},{y2}')
        start, end = list(sorted([y1, y2]))
        for y in range(start, end + 1):
            self._increment_height(x, y)

    def draw(self, line):
        if line.is_diagonal():
            print('Not drawing diagonal line')
            return
        if line.is_horizontal():
            self._draw_horizontal(line.p1.x, line.p2.x, line.p1.y)
        else:
            self._draw_vertical(line.p1.x, line.p1.y, line.p2.y)
    
    def get_depth_count(self, threshold = 2):
        count = 0
        for row in self.heights.values():
            for height in row.values():
                count += 1 if height >= threshold else 0
        return count
    
    def __repr__(self) -> str:
        return str(self.heights)


lines = []
for line in sys.stdin:
    lines.append(
        Line(
            *list(
                map(
                    lambda s: Point(*list(map(int, s.split(',')))),
                    line.rstrip().split(' -> ')
                )
            )
        )
    )

map = Map()
for line in lines:
    map.draw(line)

print(map.get_depth_count())
