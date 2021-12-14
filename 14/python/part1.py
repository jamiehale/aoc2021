import sys

template = ''
got_template = False
rules = {}

for line in sys.stdin:
    if got_template:
        pair, insertion = line.rstrip().split(' -> ')
        rules[pair] = insertion
    else:
        if line.rstrip() == '':
            got_template = True
        else:
            template = line.rstrip()

print(f'Template:     {template}')
for n in range(10):
    output = ''
    for i, c in enumerate(template):
        output += c
        if i < (len(template) - 1):
            pair = template[i:i+2]
            insertion = rules[pair]
            output += insertion
    template = output
    print(f'After step {i+1}: {template}')

counts = {}
for c in template:
    counts[c] = counts.get(c, 0) + 1

max_letter = None
max_count = 0
min_letter = None
min_count = 100000000000
for k, v in counts.items():
    if v > max_count:
        max_letter = k
        max_count = v
    if v < min_count:
        min_letter = k
        min_count = v

print(counts)
print(f'Max: {max_letter}={max_count}')
print(f'Min: {min_letter}={min_count}')
print(max_count - min_count)
