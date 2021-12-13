import sys

openings = ['(', '{', '<', '[']
closings = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']',
}
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

class CorruptError(Exception):
    pass

class IncompleteError(Exception):
    def __init__(self, correction):
        self.correction = correction

def extract_chunks(opening, s):
    while len(s) > 0:
        print(f'Processing {s} with opening {opening}...')
        if opening is not None and s[0] == closings[opening]:
            remainder = s[1:]
            print(f'Closing {opening} with remainder {remainder}')
            return remainder
        if s[0] in openings:
            print(f'Extracting chunks from {s[1:]}')
            try:
                s = extract_chunks(s[0], s[1:])
            except IncompleteError as e:
                print(f'Continuing incomplete chain with {e.correction}')
                raise IncompleteError(e.correction + (closings[opening] if opening is not None else ''))
        else:
            print(f'Found {s[0]} when expecting {closings[opening]}')
            raise CorruptError()
    print(f'Starting incomplete chain with {closings[opening]}')
    raise IncompleteError(closings[opening])

def calculate_score(correction):
    score = 0
    for c in correction:
        score = score * 5 + points[c]
    return score

scores = []
for line in sys.stdin:
    try:
        extract_chunks(None, line.rstrip())
    except CorruptError:
        continue
    except IncompleteError as e:
        print(f'Incomplete with {e.correction}')
        scores.append(calculate_score(e.correction))

sorted_scores = sorted(scores)
print(len(sorted_scores))
print(sorted_scores[int(len(sorted_scores) / 2)])
