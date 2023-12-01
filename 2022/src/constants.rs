use std::{path::Path, fs};

pub fn get_input_file(day: u8) -> String {
    let input_path = Path::new("./inputs").join(format!("d{}", day));
    println!("{:?}", input_path);
    fs::read_to_string(input_path).unwrap()
}