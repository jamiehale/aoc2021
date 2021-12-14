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

pairs = {}
counts = {}
for i in range(len(template) - 1):
    pair = template[i:i+2]
    pairs[pair] = pairs.get(pair, 0) + 1
    counts[template[i]] = counts.get(template[i], 0) + 1
counts[template[-1]] = counts.get(template[-1], 0) + 1

for n in range(40):
    new_pairs = pairs.copy()
    for k, v in new_pairs.items():
        left_pair = k[0] + rules[k]
        right_pair = rules[k] + k[1]
        pairs[left_pair] = pairs.get(left_pair, 0) + v
        pairs[right_pair] = pairs.get(right_pair, 0) + v
        pairs[k] -= v
        counts[rules[k]] = counts.get(rules[k], 0) + v

print(counts)
print(max(counts.values()) - min(counts.values()))
