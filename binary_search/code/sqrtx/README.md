# Sqrt(x) (LC 69)

Return the integer square root of `x` (floor), without using built-in exponent functions.

## Approaches

### 1. Linear Scan
- **Time:** O(√x) | **Space:** O(1)
- Increment `i` while `(i+1)² ≤ x`. Return `i`.

### 2. Binary Search
- **Time:** O(log x) | **Space:** O(1)
- Search in range `[1, x//2]`. For each `mid`, compute `mid²`.
- If `mid² == x`, return `mid`. If `mid² < x`, record `mid` as a candidate and search right. If `mid² > x`, search left.
- When the loop ends, `hi` holds the floor of √x.

## Key Insight

We're searching for the largest integer `k` such that `k² ≤ x`. Binary search on the answer space `[1, x//2]` works because the function `k²` is monotonically increasing — if `mid²` is too small, all values left of `mid` are also too small. When the loop exits, `hi` is the last valid candidate (the floor).

## Edge Cases

- `x = 0` → return 0 (handled before the binary search).
- `x = 1` → return 1.
- Perfect squares (e.g., `x = 9`) → `mid² == x` found exactly.
- Large values (up to 2³¹ - 1): use `mid * mid` carefully; Python handles big integers natively.
- `x = 2` or `x = 3` → floor is 1 (not 2).
