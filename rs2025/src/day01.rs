use std::fs;

pub fn day01() {
    let test_file = "src/inputs/day01.test.in";
    let main_file = "src/inputs/day01.in";

    part1(&test_file);
    part1(&main_file);

    part2(&test_file);
    part2(&main_file);
}

fn part1(filename: &str) -> u32 {
    let content = fs::read_to_string(filename).expect("should have been able to read");
    let rows = content.split("\n");

    let mut curr: i32 = 50;
    let mut count: u32 = 0;

    for row in rows {
        if row.starts_with("L") {
            let delta: &i32 = &row[1..].parse().unwrap();
            curr -= delta;
        } else if row.starts_with("R") {
            let delta: &i32 = &row[1..].parse().unwrap();
            curr += delta;
        }

        if curr % 100 == 0 {
            count += 1;
        }
    }

    println!("{count}");
    count
}

fn part2(filename: &str) -> i64 {
    let content = fs::read_to_string(filename).expect("should have been able to read");
    let rows = content.split("\n");

    let mut curr: i64 = 50;
    let mut count: i64 = 0;

    for row in rows {
        let prev = curr;

        if row.starts_with("L") {
            let delta: &i64 = &row[1..].parse().unwrap();
            curr -= delta;
            if curr % 100 == 0 {
                count += 1;
            }
            if prev % 100 == 0 {
                count -= 1;
            }
        } else if row.starts_with("R") {
            let delta: &i64 = &row[1..].parse().unwrap();
            curr += delta;
        }

        let zeroes: i64 = (floor(prev) - floor(curr)).abs();
        count += zeroes;
    }

    println!("{count}");
    count
}

fn floor(mut n: i64) -> i64 {
    let mut c = 0;
    if n < 0 {
        while n < 0 {
            n += 100;
            c -= 1;
        }
    } else {
        while n > 100 {
            n -= 100;
            c += 1;
        }
    }
    return c;
}
