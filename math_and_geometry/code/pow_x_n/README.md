# LC 50 — Pow(x, n)

Implement `pow(x, n)` — compute x raised to the power n. Handle negative exponents and large n efficiently.

## Approaches

### 1. Brute Force
- **Time:** O(n) | **Space:** O(1)
- Multiply `x` by itself `n` times. Too slow for large `n` (up to 2³¹ - 1).

### 2. Fast Exponentiation (Binary Exponentiation)
- **Time:** O(log n) | **Space:** O(1)
- If `n` is odd, multiply result by `x`. Square `x` and halve `n`. Repeat until `n = 0`. For negative `n`, use `1/x` and `abs(n)`.

## Key Insight

`x^n = (x²)^(n/2)` when `n` is even, and `x × (x²)^((n-1)/2)` when `n` is odd. This halves the problem size at each step, giving O(log n) multiplications. The iterative version avoids recursion stack overhead. Handling negative exponents by inverting `x` and using `abs(n)` is cleaner than special-casing.

## Edge Cases

- `n = 0`: Return 1.0 (any number to the power 0 is 1).
- `n < 0`: Use `1/x` and `abs(n)`.
- `x = 0, n > 0`: Return 0.
- `x = 1` or `x = -1`: Result is ±1 regardless of `n`.
- `n = -2147483648` (INT_MIN): `abs(n)` must be handled carefully in languages with fixed-width integers (Python handles this natively).
