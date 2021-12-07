use std::{ io, io::prelude::* };

pub fn collect_all_positions() -> Vec<i32> {
    let mut positions: Vec<i32> = vec![];
    for line in io::stdin().lock().lines() {
        let mut line_positions: Vec<i32> = line.unwrap().split(",").map(|s| s.parse::<i32>().unwrap()).collect();
        positions.append(&mut line_positions);
    }
    positions
}

pub fn find_range(positions: &Vec<i32>) -> (i32, i32) {
    let mut min_position = positions[0];
    let mut max_position = positions[0];
    for position in positions {
        if *position < min_position {
            min_position = *position;
        }
        if *position > max_position {
            max_position = *position;
        }
    }
    (min_position, max_position)
}

pub fn calculate_fuel_costs_to(positions: &Vec<i32>, target: i32, fuel_cost_fn: fn(&i32, &i32) -> i32) -> i32 {
    let mut fuel = 0;
    for position in positions {
        fuel += fuel_cost_fn(&target, position);
    }
    fuel
}

pub fn find_min_fuel(positions: &Vec<i32>, fuel_cost_fn: fn(&i32, &i32) -> i32) -> i32 {
    let (min_position, max_position) = find_range(&positions);

    let mut min_fuel = i32::MAX;
    for target in min_position..(max_position + 1) {
        let fuel = calculate_fuel_costs_to(&positions, target, fuel_cost_fn);
        if fuel < min_fuel {
            min_fuel = fuel;
        }
    }

    min_fuel
}
