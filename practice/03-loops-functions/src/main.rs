fn is_even(number: u32) -> bool {
    number % 2 == 0
}

// Добавьте count_even_to и sum_even_to по условиям tasks.md.

fn main() {
    let limit: u32 = 10;
    println!("Верхняя граница: {}", limit);
    println!("Граница чётная: {}", is_even(limit));
    // Выведите количество и сумму после написания функций.
}

#[cfg(test)]
mod tests {
    use super::is_even;

    #[test]
    fn checks_parity() {
        assert!(is_even(0));
        assert!(!is_even(3));
    }
    // Добавьте тесты границ для новых функций.
}
