use std::{ io, io::prelude::* };

fn bit_value(n: i32, bit: i32) -> i32 {
    (n & (1 << bit)) >> bit
}

fn get_filtered_readings(readings: &Vec<i32>, bit: i32, get_value_to_match_fn: fn(i32, i32) -> i32) -> Vec<i32> {
    let mut ones = 0;
    for reading in readings {
        ones += bit_value(*reading, bit);
    }
    let value_to_match = get_value_to_match_fn(
        readings.len().try_into().unwrap(),
        ones
    );
    let mut filtered: Vec<i32> = vec![];
    for reading in readings {
        if bit_value(*reading, bit) == value_to_match {
            filtered.push(*reading);
        }
    }
    filtered
}

fn determine_rating(readings: &Vec<i32>, bit: i32, value_fn: fn(i32, i32) -> i32) -> i32 {
    if readings.len() == 1 {
        return readings[0];
    }

    determine_rating(
        &get_filtered_readings(readings, bit, value_fn),
        bit - 1,
        value_fn
    )
}

fn main() {
    let mut values: Vec<i32> = vec![];
    for line in io::stdin().lock().lines() {
        let value = i32::from_str_radix(&line.unwrap(), 2).unwrap();
        values.push(value);
    }

    let oxygen_generator_rating = determine_rating(
        &values,
        11,
        |total, x| { if x >= total - x { 1 } else { 0 } }
    );

    let co2_scrubber_rating = determine_rating(
        &values,
        11,
        |total, x| { if x < total - x { 1 } else { 0 } }
    );

    println!("{}", oxygen_generator_rating);
    println!("{}", co2_scrubber_rating);
    println!("{}", oxygen_generator_rating * co2_scrubber_rating);
}
