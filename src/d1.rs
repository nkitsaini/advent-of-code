use crate::constants;

pub fn run() {
    let input = constants::get_input_file(1);
    dbg!(solve(input));
}

fn solve(input: String) -> u64 {
    let mut current_energy = Vec::<u64>::new();
    let mut elf_energies: Vec<u64> = vec![];
    for line in input.lines() {
        if line.len() == 0 {
            elf_energies.push(current_energy.iter().sum());
            current_energy.clear();
        } else {
            current_energy.push(line.parse().unwrap());
        }
    }
    elf_energies.sort();
    dbg!(elf_energies[elf_energies.len()-3..].iter().collect::<Vec<_>>());
    elf_energies[elf_energies.len()-3..].iter().sum()
}
