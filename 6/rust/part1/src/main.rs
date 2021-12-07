use common;

fn main() {
    let ages = common::read_all_ages();
    let mut age_map = common::initialize_age_map(ages);

    for _ in 0..80 {
        age_map = common::next_day(& mut age_map);
    }

    println!("{}", age_map.values().sum::<i64>());
}
