use common::{ collect_all_positions, find_min_fuel };

fn increasing_fuel_cost(position_1: &i32, position_2: &i32) -> i32 {
    let n = (*position_1 - *position_2).abs();
    (n * (n + 1)) / 2
}

fn main() {
    let positions = collect_all_positions();
    let min_fuel = find_min_fuel(&positions, increasing_fuel_cost);
    
    println!("{}", min_fuel);
}
