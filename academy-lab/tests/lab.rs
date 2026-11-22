use academy_rust_lab::{clamp_value, count_even, double_value, sum_positive};

#[test]
fn smoke() {
    assert_eq!(double_value(21), 42);
    assert_eq!(double_value(-4), -8);
}

#[test]
fn positive_sum() {
    assert_eq!(sum_positive(&[-3, 5, 0, 2, -9]), 7);
    assert_eq!(sum_positive(&[]), 0);
    assert_eq!(sum_positive(&[-2, 0, -8]), 0);
    assert_eq!(sum_positive(&[i32::MAX, i32::MAX]), i64::from(i32::MAX) * 2);
}

#[test]
fn even_count() {
    assert_eq!(count_even(&[-4, 3, 0, 8, -5]), 3);
    assert_eq!(count_even(&[]), 0);
    assert_eq!(count_even(&[-3, 1, 5]), 0);
}

#[test]
fn clamp_bounds() {
    assert_eq!(clamp_value(-3, 0, 10), 0);
    assert_eq!(clamp_value(7, 0, 10), 7);
    assert_eq!(clamp_value(19, 0, 10), 10);
    assert_eq!(clamp_value(19, 4, 4), 4);
    assert_eq!(clamp_value(-8, -5, -2), -5);
}
