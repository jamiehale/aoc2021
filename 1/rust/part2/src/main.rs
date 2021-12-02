use std::{io, io::prelude::*};

fn main() {
    let mut window: Vec<i32> = vec![];
    let mut previous = 0;
    let mut count = 0;
    for line in io::stdin().lock().lines() {
        let n: i32 = line.unwrap().parse().unwrap();
        if window.len() < 3 {
            window.push(n);
            if window.len() == 3 {
                previous = window.iter().sum();
            }
        } else {
            window.push(n);
            window.remove(0);
            let total = window.iter().sum();
            if total > previous {
                count += 1;
            }
            previous = total;
        }
    }
    println!("{}", count);
}
