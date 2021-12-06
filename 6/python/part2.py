import sys

age_counts = {}

for line in sys.stdin:
    ages = list(map(int, line.split(',')))
    for age in ages:
        age_counts[age] = age_counts.get(age, 0) + 1

def next_day(age_counts):
    return {
        0: age_counts.get(1, 0),
        1: age_counts.get(2, 0),
        2: age_counts.get(3, 0),
        3: age_counts.get(4, 0),
        4: age_counts.get(5, 0),
        5: age_counts.get(6, 0),
        6: age_counts.get(0, 0) + age_counts.get(7, 0),
        7: age_counts.get(8, 0),
        8: age_counts.get(0, 0),
    }

for i in range(256):
    age_counts = next_day(age_counts)

print(age_counts)
print(sum(age_counts.values()))
