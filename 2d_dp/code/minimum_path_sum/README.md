# LC 64 — Minimum Path Sum

Given an `m × n` grid of non-negative numbers, find a path from top-left to bottom-right that minimizes the sum. You can only move right or down.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`. Initialize first row and column by accumulating sums (only one direction possible).

### 2. 1D DP (Space-Optimized)
- **Time:** O(m × n) | **Space:** O(n)
- Maintain a single row `dp`. For each grid row, update `dp[j] = min(dp[j], dp[j-1]) + grid[i][j]`. `dp[j]` (before update) holds the value from the row above; `dp[j-1]` holds the value from the left.

## Key Insight

At each cell, the minimum path sum is the cell's value plus the minimum of coming from above or from the left. The 1D optimization works because when processing cell `(i, j)`, `dp[j]` still holds the result from row `i-1` (above), and `dp[j-1]` already holds the result from `(i, j-1)` (left).

## Edge Cases

- Single cell: Return `grid[0][0]`.
- Single row: Only rightward movement, sum all cells.
- Single column: Only downward movement, sum all cells.
- All zeros: Return 0.
