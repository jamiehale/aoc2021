import sys

horizontal_position = 0
depth = 0

for line in sys.stdin:
    instruction, distance = line.rstrip().split(' ')

    if instruction == "forward":
        horizontal_position += int(distance)
    elif instruction == "down":
        depth += int(distance)
    elif instruction == "up":
        depth -= int(distance)

print(horizontal_position)
print(depth)
print(horizontal_position * depth)
    
