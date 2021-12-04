import sys

def bit_value(n, bit):
    return (n & (1 << bit)) >> bit

def get_value_to_match(readings, bit, value_fn):
    count = 0
    for reading in readings:
        if bit_value(reading, bit) == 1:
            count += 1
    return value_fn(readings, count)

def get_filtered_readings(readings, bit, value_fn):
    value_to_match = get_value_to_match(readings, bit, value_fn)
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
readings = []

for line in sys.stdin:
    readings.append(int(line, 2))

oxygen_generator_rating = determine_rating(
    list(readings),
    width - 1,
    lambda readings, count: 1 if count >= len(readings) - count else 0
)

co2_scrubber_rating = determine_rating(
    list(readings),
    width - 1,
    lambda readings, count: 1 if count < len(readings) - count else 0
)

print(oxygen_generator_rating)
print(co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)
