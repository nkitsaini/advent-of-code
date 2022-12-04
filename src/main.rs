mod d1;
mod constants;
mod d2;

const DAY: u8 = 1;

fn main() {
    let input = constants::get_input_file(DAY);
    dbg!(d2::solve(input));
}
