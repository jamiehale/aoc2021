import sys

counts = [0] * 12
count = 0

for line in sys.stdin:
    count += 1
    number = int(line, 2)
    for i in range(12):
        mask = 1 << i
        if number & mask:
            counts[i] += 1

gamma = 0
epsilon = 0

for i in range(12):
    if counts[i] > count - counts[i]:
        gamma |= 1 << i
    elif counts[i] < count - counts[i]:
        epsilon |= 1 << i

print(gamma)
print(epsilon)
print(gamma * epsilon)