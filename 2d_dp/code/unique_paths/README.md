# LC 62 — Unique Paths

A robot at the top-left of an `m × n` grid can only move right or down. Count the number of unique paths to the bottom-right corner.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. First row and column are all 1s (only one way to reach them).

### 2. 1D DP
- **Time:** O(m × n) | **Space:** O(n)
- Maintain one row. For each new row, `dp[j] += dp[j-1]`. The current `dp[j]` (before update) is the value from above; `dp[j-1]` is from the left.

### 3. Combinatorics
- **Time:** O(m + n) | **Space:** O(1)
- The robot makes exactly `m-1` down moves and `n-1` right moves in any order. Answer is `C(m+n-2, n-1)` — choose which steps are rightward.

## Key Insight

Every path consists of exactly `(m-1) + (n-1)` moves. The combinatorics solution is the most elegant: we're choosing which `n-1` of the total moves are rightward. The DP approaches build up the count by summing paths from above and from the left.

## Edge Cases

- `m = 1` or `n = 1`: Only one path (straight line). Return 1.
- `m = n = 1`: Already at destination. Return 1.
- Large `m, n` (up to 100): Combinatorics avoids large intermediate DP tables.
