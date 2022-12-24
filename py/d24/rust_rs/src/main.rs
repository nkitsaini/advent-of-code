use std::{sync::Arc, collections::HashSet};

use strum::IntoEnumIterator;


const SAMPLE: &'static str = "#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#";

const DATA: &'static str = "#.########################################################################################################################
#<<<^<^^>v<<^<^><><v<^<<.v^><<<v>><^v<vv>v<vv>^>>^^^^.>>^vv<^<<>^.vv.<>>v>v^>^<><.vv^v.^<^v>^vv<^vv<<>v<<>><<<v^^>v><<<^>#
#>^^v><.<>>v.v.^>v^..>^<vv>v^><v^<<>v>>.^v^vv^^>.^><^>>^>vv>>v^>vvvv^v^vv<<^<^>^>^v<v^>><><v^^^<v.^v<>^.>v><vv.^<^^^^<>>>#
#<<.><>v<>.v^<^^v<^^>.^.>>v.^^^v>^^^.<><.^.<>>^<>.v><^^^>^>^^^^><vv^.v^<<^v>v^^^<<<^<..^vv><.^v<vv^>>vv>v.><v^>>^<v^>>vv>#
#.><^v.>^v>>vv><^>.>>>>>^.>>.>^v>v^>v^^>v^^..>^.^<^.v<>v<<<^^^.vvv>>.<>^vvv>>.^<^v^>^<^<vv>^>^.<>^<<>v.<<<.^<>^>.<v.vvv^>#
#>><v<>.v><<^^vvv<<<^>^v^v><^>^<>>v.<.<>^<>vv>vv>^.v><<<^<v^vvv.<<<><^<^<^.^^vv>^v^^v<>>vv^<^.^v^v<v^>^.>.v>v^^<v<^<>^>v>#
#>>><v<.>>v^<.^vvvv<v<^<<v>>v>vv.^><v^.>>vv><<.<^.^v>^^><>^<^v<vvvvv<<<<^^>..>>>v^^>.vv<>.^^^.<v>v^>>^>^^>v^v^^<.>>^^<.<>#
#<<v>>v<>^><^v<>^>vvv..v.^.<^.v.vv^.<.v<>v>^<^v^<^>><.<>v^v>^<<^<v^^<v^<v^.<v><<<>^^<><>.v><^^^<<^<v>><vv<^<^.^<<^.^<<v>>#
#>>>^^>v^>^>>v><<>^<v><>>^>.<v<<>v<>^<>^v.<<^.^^^^>^.v>v><v^>vv^^^.>v^<v^^v<<^.vv^>vvv>^>>v<.^^vv<<v.v..^v.^vvv.<.>^<^v>>#
#><^vv^>>v.<^<v^^><v^>^><<<v^>v><v^^>><vv^><.>>^vv>><vv<^v^v^>^>>.vvvvvv<>>>.>^<vv^<vv<<<^^v^>.v><^.<<^<>^^>.^v><^^vv.^>>#
#>..<<v<<>>.<^v<<.>v^<..^<^^v^>.><.<v>>v><<>^>>v<vvv>>v<v>.vvvv<.<<<^<^v>^<v^>>v.^v^<^v..^..<^<><>^<<>^>^<<^^.>^^<v<>v<><#
#<v^v>v<^^<v>>vv^v<..^>v>>>.>^^<>>>^..>>>^<<^<^<>^<v>>^>>><^v^v^<.^<<<^v^.^^^<v>>><^^<>>><..vv.^.^<<v^v.>>^v^^><>><.v^>v>#
#.<^^<v>v.<v<^.^v^<.v^vvv^vv^<..v<.>>>v<<>>vv>>^.>^.v>vv>.v^<<v^>>v.<^^<^<<>^^.^^>^>>^<^<<^^vv^^.<.><^.>^^<>v<.^v<>v><v<.#
#>^.v^^><^<.>^v>v><>>>..>.v>vvv<<vv^.>v>.>v.<^vv.^>^vvv>.>v^v>>.>^^<<>>.^.>>>^>v<>v>v^^<>^<^.^><.vv^^<<.^v>>.>>>.^>^^^^^<#
#..^>vv><^^.>>^^.<<<v..<<>^.<.<^^.v<<<^<<>><>v>v<^^^.<><^<<>v^^<^v^>^v>v<<^<<v<><<>.><..<^vv^<.><>^^><<.>>^.^v><>v^<^v>^>#
#><<>v>.>^<<v>>>>>^>v..<vv<^<v>>^<<^v<v<<<<.v^>v.v<^>>>v.^><^><>.<>.^v><><<v>^^^^.<<.>^>><>.<<.<^<.^>..^>^.^>^v^v.<.^v>><#
#><><^v.<<<<>>v<<<<^v<<^^<><<.>^^.^.^.<>vv<<<v>^<><^^<^>^>^^.v<^>>vv^v.>^.<<><vv>>.>.<><^<.<<>.v>.^>>>^<<>.<v>^^v^v^<>.<<#
#<^>^v^>v^v.<^^>.^>^<<>.<.<<vvv>v>v^v^vvv>v^v^v<^^^<^>>v.^v.^>v><.^^^<>^>^^vv.v>>>^v<<>>^<^.v^>>>><v>v><^<.^v^v^^.<<>><^<#
#>^>v.><v<^<><>><v<^^<^><<<<^v>^<v^>v<<>^>>.><v<v<^^>^<><><^<.<.<><v^^.^>>v^v^.>><vvvv^v^vv><<^<<^>.v>>>vv>v^v^^<v^^>^>><#
#<<v^^>vv^^v.<<v<v<^><^v.>.<^v^>^^>^<^^v>>v<^^vv<>^v^.^v<>.<^^>^^v><>^^v.><.v^^>.<<.v^<v<^<>^<^><v^>.>^v>v<v<.>v<.<v.>.<<#
#>^<<v^vv..vv^v><>>>^>v.>v^..^>^vv>^^>v^v<>.><v<<<<^><>v^.v^>.>^vv>vv>.>^<<.v<^^v^<<>^^^>^.<.v>^><.<^<^>>><.<<^^^>^<^<v<>#
#<^><v<v><<<>v>>vv.>^<v>><>v>^.v^<v><<^<>>^<^^.<v<<vv>^v.v.<vv<^<<^>v>v.<<<v^><^^>.>>v>.<^vv.^v>^^^<><<^<>>><v^v>>>v<^>v>#
#>>>^.v><<<>^v<.<.^><v>><>.<.<>v^v>>>^<^^vvv.vv<v<^^^>><^v>>>v>v<>v<v<vv^.^>v<>^>>>^<<v<vv^>><.v<^v<v^<.<>v>^>^><.>v<>.><#
#<^<v>v.vv>vv^v<.>>.v.^..>^v<.v><>^<.^^<v><^.v^<v^vv^^v^<>>^<^><v.vvv^>.^v>><<>><<<>.<v^<^.<vv^.v<><v^v^>^v^>v<<v^>vv>^v>#
#<><.v.^v>>><^.<.^<<v>^^><<^>>.^^.v>vv^^.v>^<<^^<<<^>>^>^>v..^v><>v<vv<<v^v<>>><v>^v<><.>v>v>v^^.^>>vv^v.vv<>v^<><^^><vv<#
#<<v<v>^><^v^<^<v>><.v<.>^vv^>^<v^v>v<.vvv<v<^^>^^^^v^<<v^>v<v^vv>.^vv>v^.>>.^<.>>v<..^v.>^<<v<vvv^<..^<<>^^>v<<><^^><>>>#
########################################################################################################################.#";

#[derive(Debug, Copy, Clone, Hash, PartialEq, Eq, strum_macros::EnumIter)]
enum Direction {
    Up,
    Down,
    Left,
    Right
}

impl Direction {
    fn to_char(&self) -> char {
        match self {
            Self::Up => '^',
            Self::Down => 'v',
            Self::Left => '<',
            Self::Right => '>',
        }

    }
    fn from_char(chr: char) -> Option<Self> {
        match chr {
            '>' => Some(Direction::Right),
            '<' => Some(Direction::Left),
            '^' => Some(Direction::Up),
            'v' => Some(Direction::Down),
            _ => None
        }
    }
    
    fn cords(&self) -> (i8, i8) {
        match self {
            Self::Up => (-1, 0),
            Self::Down => (1, 0),
            Self::Left => (0, -1),
            Self::Right => (0, 1),
        }

    }
}

#[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
struct Position {
    i: usize,
    j: usize
}
impl From<(usize, usize)> for Position {
    fn from(value: (usize, usize)) -> Self {
        return Position { i: value.0, j: value.1 }
    }
}

impl Position {
    fn step(&self, direction: Direction) -> (i64, i64) {
        let (di, dj) = direction.cords();
        let ni = self.i as i64 + di as i64;
        let nj = self.j as i64 + dj as i64;
        (ni, nj)
    }
}

#[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
struct Flake {
    direction: Direction,
    position: Position
}

#[derive(Debug, Clone, Copy, Hash, PartialEq, Eq)]
struct BoardOptions {
    min_i: usize,
    max_i: usize,
    min_j: usize,
    max_j: usize
}

impl BoardOptions {
    fn is_safe_me(&self, i: i64, j: i64) -> bool {
        if (i, j) == (0, 1) || (i, j) == (self.max_i as i64+1, self.max_j as i64) {
            return true
        }
        let (ni, nj) = (i, j);
        let bo = *self;
        let mut new_cords = None;

        if bo.min_i as i64 > ni {
            new_cords = Some((bo.max_i as i64, nj));
        }
        if (bo.max_i as i64) < ni {
            new_cords = Some((bo.min_i as i64, nj));
        }
        if (bo.max_j as i64) < nj {
            new_cords = Some((ni, bo.min_j as i64));
        }
        if (bo.min_j as i64) > nj {
            new_cords = Some((ni, bo.max_j as i64));
        }
        return new_cords.is_none()

    }
}

impl Flake {
    fn step(&self, bo: BoardOptions) -> Flake {
        let (ni, nj) = self.position.step(self.direction);
        let mut new_cords: Option<(i64, i64)> = None;
        if bo.min_i as i64 > ni {
            new_cords = Some((bo.max_i as i64, nj));
        }
        if (bo.max_i as i64) < ni {
            new_cords = Some((bo.min_i as i64, nj));
        }
        if (bo.max_j as i64) < nj {
            new_cords = Some((ni, bo.min_j as i64));
        }
        if (bo.min_j as i64) > nj {
            new_cords = Some((ni, bo.max_j as i64));
        }
        if new_cords.is_none() {
            new_cords = Some((ni, nj));
        }
        let new_cords = new_cords.unwrap();

        return Flake { direction: self.direction, position: Position { i: new_cords.0 as usize, j: new_cords.1 as usize } }

    }
}

#[derive(Debug, Hash, PartialEq, Eq, Clone)]
struct Field {
    flakes: Vec<Flake>,
    board_options: BoardOptions
}

impl Field {
    fn from_string(value: &str) -> Self {
        let mut flakes = vec![];
        for (i, line) in value.lines().enumerate() {
            for (j, chr) in line.chars().enumerate() {
                if let Some(d) = Direction::from_char(chr) {
                    flakes.push(Flake {direction: d, position: Position {i, j}});
                }
            }
        }
        Self {
            flakes,
            board_options: BoardOptions { min_i: 1, max_i: value.lines().count()-2, min_j: 1, max_j: value.lines().nth(0).unwrap().len()-2 }
        }
    }
    fn step(&self) -> Self {
        let mut new_flakes = vec![];
        for flake in self.flakes.iter() {
            new_flakes.push(flake.step(self.board_options))
        }
        Field {flakes: new_flakes, board_options: self.board_options}
    }
    fn repr(&self) -> String {
        let height = self.board_options.max_i + 2;
        let width = self.board_options.max_j + 2;

        #[derive(Debug, Clone, Copy)]
        enum Box {
            Empty,
            One(Direction),
            Multi{count: u64},
            Wall
        }

        impl Box {
            fn to_char(&self) -> char {
                match self {
                    Self::Empty => '.',
                    Self::One(direction) => direction.to_char(),
                    Self::Multi { count } => {
                        let count_str = format!("{count}");
                        assert!(count_str.len() == 1, "Multi width: {}", &count_str);
                        count_str.chars().next().unwrap()
                    },
                    Self::Wall => '#'
                }
            }
            fn add(&mut self, direction: Direction) {
                // TODO: inplace replace
                let new_box = match self {
                    Self::Empty => Self::One(direction),
                    Self::One(_) => Self::Multi { count: 2 },
                    Self::Multi { count } => Self::Multi { count: *count+1 },
                    Self::Wall => unreachable!()
                };
                let _ = std::mem::replace(self, new_box);
            }
        }

        let mut rv = vec![vec![Box::Empty; width]; height];
        for i in 0..height {
            rv[i][0] = Box::Wall;
            rv[i][width-1] = Box::Wall;
        }
        for j in 0..width {
            rv[0][j] = Box::Wall;
            rv[height-1][j] = Box::Wall;
        }

        for flake in self.flakes.iter() {
            let position = flake.position;
            let direction = flake.direction;
            rv[position.i][position.j].add(direction);
        }

        let a = rv.into_iter().map(|x| {
            x.into_iter().map(|x| format!("{}", x.to_char())).collect::<Vec<String>>().join("")
            // return 1
        }).collect::<Vec<String>>().join("\n");
        a

    }
    fn is_empty(&self, pos: Position) -> bool {
        for flake in self.flakes.iter() {
            if flake.position == pos {
                return false
            }
        }
        return true
    }
    fn is_empty_cords(&self, i: i64, j: i64) -> bool {
        self.board_options.is_safe_me(i, j) && self.is_empty(Position {i: i as usize, j: j as usize})
    }
}

#[derive(Debug, Hash, PartialEq, Eq, Clone)]
struct State {
    field: Arc<Field>,
    steps: u64,
    position: Position
}
impl State {
    fn next_states(&self) -> Vec<Self> {
        let next_field = self.field.step();
        let arc_field = Arc::new(next_field.clone());
        let mut rv = vec![];
        // move
        for direction in Direction::iter() {
            let (ni, nj) = self.position.step(direction);
            if next_field.is_empty_cords(ni, nj){
                rv.push(State {
                    field: arc_field.clone(),
                    steps: self.steps + 1,
                    position: Position { i: ni as usize, j: nj as usize }
                });
            }
        }
        if next_field.is_empty(self.position) {
                rv.push(State {
                    field: arc_field.clone(),
                    steps: self.steps + 1,
                    position: self.position
                });
        }
        rv
    }
    fn repr(&self) -> String {
        let rv = self.field.repr();
        rv.lines().into_iter().enumerate().map(|(i, line)| {
            if i == self.position.i {
                let mut rv = line.to_string();
                rv.replace_range(self.position.j..self.position.j+1, "E");
                rv
            } else {
                line.to_string()
            }
        }).collect::<Vec<String>>().join("\n")
    }
}

fn main() {
    let field = Field::from_string(SAMPLE);
    let end = Position {i: field.board_options.max_i+1, j: field.board_options.max_j};

    let state = State{
        field: Arc::new(field.clone()),
        steps: 0,
        position: Position { i: 0, j: 1 }
    };
    let mut states = vec![state];
    let mut visited: HashSet<State> = Default::default();
    loop {
        let mut new_states = vec![];
        for state in states.iter() {
            for new_state in state.next_states() {
                if !visited.contains(&new_state) {
                    if new_state.position == end {
                        println!("{}", new_state.repr());
                        dbg!(new_state.position);
                        dbg!(new_state.steps);
                        return;
                    }
                    new_states.push(new_state.clone());
                }
            }
            visited.insert(state.clone());
        }
        states = new_states;
    }
}
