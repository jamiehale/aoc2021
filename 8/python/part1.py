import sys

unique_count = 0

for line in sys.stdin:
    digits, outputs = list(
        map(
            lambda s: list(
                map(
                    lambda t: ''.join(sorted(t)),
                    s.split(' ')
                )
            ),
            line.rstrip().split(' | ')
        )
    )

    for output in outputs:
        if len(output) in [2, 3, 4, 7]:
            unique_count += 1

print(unique_count)
