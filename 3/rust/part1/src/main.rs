use std::{ io, io::prelude::* };

fn main() {
    let mut values: Vec<i32> = vec![];
    for line in io::stdin().lock().lines() {
        let value = i32::from_str_radix(&line.unwrap(), 2).unwrap();
        values.push(value);
    }
    let count: i32 = values.len().try_into().unwrap();

    let mut counts: Vec<i32> = vec![0; 12];
    for value in values {
        for i in 0..12 {
            let mask = 1 << i;
            counts[i] += (value & mask) >> i;
        }
    }

    let mut epsilon = 0;
    let mut gamma = 0;

    for i in 0..12 {
        if counts[i] > (count - counts[i]) {
            gamma |= 1 << i;
        }
        else if counts[i] < (count - counts[i]) {
            epsilon |= 1 << i;
        }
    }

    println!("{}", gamma * epsilon);
}
