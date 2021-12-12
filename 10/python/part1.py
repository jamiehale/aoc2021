import sys

openings = ['(', '{', '<', '[']
closings = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']',
}
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def extract_chunks(opening, s):
    while len(s) > 0:
        print(f'Processing {s} with opening {opening}...')
        if opening is not None and s[0] == closings[opening]:
            remainder = s[1:]
            print(f'Closing {opening} with remainder {remainder}')
            return 0, remainder
        if s[0] in openings:
            print(f'Extracting chunks from {s[1:]}')
            score, remainder = extract_chunks(s[0], s[1:])
            if score > 0:
                return score, None
            s = remainder
        else:
            print(f'Found {s[0]} when expecting {closings[opening]}')
            return scores[s[0]], s
    return 0, s

def parse(s):
    score, remainder = extract_chunks(None, s)
    return score

score = 0
for line in sys.stdin:
    score += parse(line.rstrip())

print(score)
