use lru::LruCache;
use std::collections::HashMap;

#[derive(Debug, Clone)]
struct Valve {
    name: String,
    id: usize,
    rate: usize,
    tunnels: Vec<String>,
}

impl Valve {
    fn from_line(line: &str, id: usize) -> Self {
        dbg!(line);
        let x: Vec<_> = line.split(";").collect();
        let name = x[0].split(" ").nth(1).unwrap();
        let rate: usize = x[0]
            .split(" ")
            .nth(4)
            .unwrap()
            .split("=")
            .nth(1)
            .unwrap()
            .parse()
            .unwrap();

        let tunnels: Vec<_> = x[1][23..]
            .replace(" ", "")
            .trim()
            .split(",")
            .map(|x| x.to_string())
            .collect();
        return Self {
            name: name.to_string(),
            id,
            rate,
            tunnels,
        };
    }
}

fn get_pressure_releasable(
    current_valve: String,
    open_valves: u64,
    time_left: u64,
    valves: &HashMap<String, Valve>,
    cache: &mut LruCache<(String, u64, u64), u64>,
) -> u64 {
    let key = (current_valve.clone(), open_valves, time_left);
    if let Some(x) = cache.get(&key) {
        return *x;
    }

    let valve = valves.get(&current_valve).unwrap();
    if open_valves & (1 << valve.id) == 0 {
        // Can be opened
    }

    todo!()
}

pub fn solve(content: String) -> u64 {
    let mut valves: HashMap<String, Valve> = Default::default();
    for (idx, line) in content.lines().enumerate() {
        let valve = Valve::from_line(line, idx);
        valves.insert(valve.name.clone(), valve);
    }

    let mut cache = LruCache::new(100000.try_into().unwrap());
    let ans = get_pressure_releasable("AA".to_string(), 0, 30, &valves, &mut cache);
    dbg!(ans);
    // dbg!(valves);
    todo!()
}
