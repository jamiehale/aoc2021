import sys

def to_bit(c):
    return ord(c) - ord('a')

def to_bitmask(s):
    mask = 0
    for c in ''.join(sorted(s)):
        mask |= (1 << to_bit(c))
    return mask

def bits_set(n):
    count = 0
    for i in range(7):
        if n & 1:
            count += 1
        n >>= 1
    return count

def bitmask_to_str(n):
    s = ''
    for i in range(7):
        s += '1' if n & 1 else '0'
        n >>= 1
    return s[::-1]

total = 0
for line in sys.stdin:
    digits, outputs = list(
        map(
            lambda s: list(
                map(
                    to_bitmask,
                    s.split(' ')
                )
            ),
            line.rstrip().split(' | ')
        )
    )

    bits_1 = next(x for x in digits if bits_set(x) == 2)
    solution = {
        bits_1: 1,
    }
    digits.remove(bits_1)

    bits_7 = next(x for x in digits if bits_set(x) == 3)
    solution[bits_7] = 7
    digits.remove(bits_7)
    segments = {
        'a': bits_7 & ~bits_1
    }

    bits_4 = next(x for x in digits if bits_set(x) == 4)
    solution[bits_4] = 4
    digits.remove(bits_4)

    bits_8 = next(x for x in digits if bits_set(x) == 7)
    solution[bits_8] = 8
    digits.remove(bits_8)

    bits_4_and_7 = bits_7 | bits_4
    # print(bits_4_and_7, bitmask_to_str(bits_4_and_7))

    bits_9 = [x for x in digits if x & bits_4_and_7 == bits_4_and_7 and bits_set(x & ~bits_4_and_7) == 1][0]
    solution[bits_9] = 9
    digits.remove(bits_9)
    segments['g'] = bits_9 & ~bits_4_and_7
    segments['e'] = bits_8 & ~bits_9

    some_bits = bits_7 | segments['g']
    bits_3 = [x for x in digits if (x & some_bits == some_bits) and (bits_set(x & ~some_bits) == 1)][0]
    solution[bits_3] = 3
    digits.remove(bits_3)
    segments['d'] = bits_3 & ~some_bits
    segments['b'] = bits_4 & ~(bits_1 | segments['d'])
    # segments['c'] = bits_1 &

    bits_0 = bits_8 & ~segments['d']
    solution[bits_0] = 0
    digits.remove(bits_0)

    bits_6 = [x for x in digits if bits_set(x) == 6][0]
    solution[bits_6] = 6
    digits.remove(bits_6)
    segments['c'] = bits_8 & ~bits_6
    segments['f'] = bits_1 & ~segments['c']

    solution[bits_8 & ~segments['b'] & ~segments['f']] = 2
    solution[bits_6 & ~segments['e']] = 5

    value = 0
    for output in outputs:
        value *= 10
        value += solution[output]

    total += value

    print(sorted(segments.keys()), sorted(solution.values()), value)

print(total)
