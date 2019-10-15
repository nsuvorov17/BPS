use std::io;
fn main() {
    loop {
        println!("Enter the term that you want to generate!");
        let mut term = String::new();
        io::stdin().read_line(&mut term)
            .ok()
            .expect("Failed to read line!");
        // convert string to int
        let term: usize = match term.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Please enter a valid number!");
                continue;
            }
        };
        // Get the fib term
        //let fib_number = get_fib_term_dynamic(term);
        let fib_total = get_fib_term_dynamic(term-1) + get_fib_term_dynamic(term+1);
        println!("{}", fib_total);
        break;
        
        
    }
}

fn get_fib_term_dynamic(term: usize) -> u32 {
    let mut v = vec![0u32, 1];
    for i in 2..(term+1) {
        let sum = v[i-1] + v[i-2];
        v.push(sum);
    }
    return v[term];
}