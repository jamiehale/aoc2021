use std::{io, io::prelude::*};
use std::collections::HashMap;

pub fn read_all_ages() -> Vec<i32> {
    let mut ages: Vec<i32> = vec![];
    for line in io::stdin().lock().lines() {
        let mut new_ages: Vec<i32> = line.unwrap().split(",").map(|s| s.parse::<i32>().unwrap()).collect();
        ages.append(&mut new_ages);
    }
    ages
}

pub fn initialize_age_map(ages: Vec<i32>) -> HashMap<i32, i64> {
    let mut age_map = HashMap::new();
    for age in ages {
        let count = age_map.entry(age).or_insert(0);
        *count += 1;
    }
    age_map
}

fn ith_next_value(ages: &mut HashMap<i32, i64>, i: i32) -> i64 {
    let mut value = *ages.entry((i + 1) % 9).or_default();
    if i == 6 {
        value += *ages.entry(0).or_default();
    }
    value
}

pub fn next_day(ages: &mut HashMap<i32, i64>) -> HashMap<i32, i64> {
    let mut new_age_map: HashMap<i32, i64> = HashMap::new();
    for i in 0..9 {
        new_age_map.insert(i, ith_next_value(ages, i));
    }
    new_age_map
}
