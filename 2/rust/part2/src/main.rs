use std::{io, io::prelude::*};

enum Instruction {
    Forward(i32),
    Up(i32),
    Down(i32),
}

fn decode_instruction<'a>(s: &'a String) -> (&'a str, i32) {
    let tuple: Vec<&str> = s.split(" ").collect();
    let instruction = tuple[0];
    let distance: i32 = tuple[1].parse().unwrap();
    (instruction, distance)
}

fn parse_instruction(s: String) -> Instruction {
    let decoded = decode_instruction(&s);
    match decoded.0.as_ref() {
        "forward" => Instruction::Forward(decoded.1),
        "up" => Instruction::Up(decoded.1),
        "down" => Instruction::Down(decoded.1),
        _ => panic!("Invalid instruction")
    }
}

fn main() {
    let mut horizontal_position = 0;
    let mut depth = 0;
    let mut aim = 0;
    for line in io::stdin().lock().lines() {
        match parse_instruction(line.unwrap()) {
            Instruction::Forward(distance) => {
                horizontal_position += distance;
                depth += aim * distance
            }
            Instruction::Up(distance) => aim -= distance,
            Instruction::Down(distance) => aim += distance,
        }
    }
    println!("{}", horizontal_position * depth);
}
