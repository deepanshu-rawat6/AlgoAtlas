# Generate Binary Strings Without Consecutive 1s

Generate all binary strings of length `n` that do not contain two consecutive `1`s.

## Approaches

### 1. Backtracking
- **Time:** O(2ⁿ) | **Space:** O(n) call stack
- At each position, always place `'0'`. Place `'1'` only if the last character is not `'1'`. When the string reaches length `n`, add it to results.

## Key Insight

The constraint "no consecutive 1s" is a local constraint: it only depends on the immediately preceding character. This makes backtracking natural — we prune the `'1'` branch whenever the last character was `'1'`. The number of valid strings of length `n` follows the Fibonacci sequence (Fibonacci strings), so the count grows as O(φⁿ) where φ ≈ 1.618.

## Edge Cases

- `n = 1`: Both `"0"` and `"1"` are valid.
- `n = 2`: `"00"`, `"01"`, `"10"` are valid; `"11"` is not.
- `n = 3`: 5 valid strings: `"000"`, `"001"`, `"010"`, `"100"`, `"101"`.
- Large `n`: The number of valid strings grows as Fibonacci(n+2).
