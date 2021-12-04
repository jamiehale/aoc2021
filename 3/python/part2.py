import sys

def bit_value(n, bit):
    return (n & (1 << bit)) >> bit

def get_filtered_readings(readings, bit, get_value_to_match_fn):
    ones = list(filter(lambda reading: bit_value(reading, bit) == 1, readings))
    value_to_match = get_value_to_match_fn(len(readings), len(ones))
    return list(filter(lambda reading: bit_value(reading, bit) == value_to_match, readings))

def determine_rating(readings, bit, value_fn):
    if len(readings) == 1:
        return readings[0]
    
    return determine_rating(
        get_filtered_readings(readings, bit, value_fn),
        bit - 1,
        value_fn
    )

width = 12
all_readings = []

for line in sys.stdin:
    all_readings.append(int(line, 2))

oxygen_generator_rating = determine_rating(
    all_readings,
    width - 1,
    lambda total, x: 1 if x >= total - x else 0
)

co2_scrubber_rating = determine_rating(
    all_readings,
    width - 1,
    lambda total, x: 1 if x < total - x else 0
)

print(oxygen_generator_rating)
print(co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)
