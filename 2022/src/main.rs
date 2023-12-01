mod constants;
mod d1;
mod d16;
mod d2;

const DAY: u8 = 16;

fn main() {
    let input = constants::get_input_file(DAY);
    dbg!(d16::solve(input));
}
