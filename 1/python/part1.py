import sys


count = 0
is_first_line = True

for line in sys.stdin:
    n = int(line)
    if is_first_line:
        is_first_line = False
    else:
        if n > previous:
            count += 1
    
    previous = n

print(count)
