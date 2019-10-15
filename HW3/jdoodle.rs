use std::io;

fn main() {
    let mut input_text = String::new();
    io::stdin()
        .read_line(&mut input_text)
        .expect("failed to read from stdin");
        
    let a: i32 = input_text.parse().unwrap();
    let _f = 0;
    let _g = 0;
    let _d = 1;
    while _d < a {
        let _f = _g + _d;
        let _g = _d;
        let _d = _f;
    }
    let s = _g + _d;
    let _i = s;

    let trimmed = input_text.trim();
    match trimmed.parse::<u32>() {
        Ok(_i) => println!("your integer input: {}", _i),
        Err(..) => println!("this was not an integer: {}", trimmed),
    };
}