# LC 1137 — N-th Tribonacci Number

The Tribonacci sequence: T(0) = 0, T(1) = 1, T(2) = 1, T(n) = T(n-1) + T(n-2) + T(n-3) for n ≥ 3. Return T(n).

## Approaches

### 1. DP Array
- **Time:** O(n) | **Space:** O(n)
- Fill `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]` from base cases. Straightforward extension of Fibonacci to three terms.

### 2. Space-Optimized (Three Variables)
- **Time:** O(n) | **Space:** O(1)
- Keep only `a, b, c` representing T(n-2), T(n-1), T(n). Roll: `a, b, c = b, c, a + b + c`.

## Key Insight

Like Fibonacci but summing the last three values instead of two. Only the three most recent values are needed at any point, so O(1) space is achievable. The base cases T(0)=0, T(1)=1, T(2)=1 must be handled before the loop starts.

## Edge Cases

- `n = 0`: Return 0.
- `n = 1` or `n = 2`: Return 1.
- `n = 37` (max constraint): T(37) = 2082876103, fits in a 32-bit integer.
