# LC 70 — Climbing Stairs

You are climbing a staircase that takes `n` steps to reach the top. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

## Approaches

### 1. Recursion with Memoization
- **Time:** O(n) | **Space:** O(n)
- Cache `dp(i)` = ways to reach step `i`. Each call reduces to `dp(i-1) + dp(i-2)`, so each subproblem is solved once.

### 2. Bottom-up DP
- **Time:** O(n) | **Space:** O(n)
- Fill `table[i] = table[i-1] + table[i-2]` iteratively from base cases `table[0] = table[1] = 1`.

### 3. Space-Optimized (Two Variables)
- **Time:** O(n) | **Space:** O(1)
- Only the last two values matter. Roll `a, b = b, a + b` at each step — no array needed.

## Key Insight

The number of ways to reach step `i` equals the sum of ways to reach `i-1` (take 1 step) and `i-2` (take 2 steps). This is exactly the Fibonacci recurrence. The answer is `fib(n+1)`.

## Edge Cases

- `n = 1`: Only one way (single step). Return 1.
- `n = 2`: Two ways (1+1 or 2). Return 2.
- The constraint `1 <= n <= 45` keeps values within standard integer range.
