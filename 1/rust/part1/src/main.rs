use std::{io, io::prelude::*};

fn main() {
    let mut first = true;
    let mut previous = 0;
    let mut count = 0;
    for line in io::stdin().lock().lines() {
        let n: i32 = line.unwrap().parse().unwrap();
        if first {
            first = false;
        } else {
            if n > previous {
                count += 1;
            }
        }
        previous = n;
    }
    println!("{}", count);
}
