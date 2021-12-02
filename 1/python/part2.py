import sys
import math


count = 0
window = []
previous = 0

for line in sys.stdin:
    n = int(line)
    if len(window) < 3:
        window.append(n)
        if len(window) == 3:
            previous = sum(window)
    else:
        window.append(n)
        window.pop(0)
        total = sum(window)
        if total > previous:
            count += 1
    
        previous = total

print(count)
