# LC 322 — Coin Change

Given an array `coins` of denominations and an integer `amount`, return the fewest number of coins needed to make up that amount. Return -1 if it's impossible. Each coin can be used unlimited times.

## Approaches

### 1. Top-down Memoization
- **Time:** O(amount × n) | **Space:** O(amount)
- `dp(rem) = 1 + min(dp(rem - c) for each coin c)`. Memoize to avoid recomputing the same remainder.

### 2. Bottom-up DP
- **Time:** O(amount × n) | **Space:** O(amount)
- Initialize `dp[0] = 0`, `dp[i] = inf`. For each amount `i`, try every coin `c <= i` and take `min(dp[i], 1 + dp[i-c])`. Build up from smaller amounts.

## Key Insight

This is an unbounded knapsack variant. The recurrence `dp[i] = 1 + min(dp[i-c])` works because we want the minimum number of steps to reach `i`, and each coin is one step. Building from `dp[0] = 0` upward ensures all subproblems are solved before they're needed.

## Edge Cases

- `amount = 0`: Answer is 0 (no coins needed).
- No combination reaches `amount`: Return -1 (check for `inf` in dp table).
- Single coin equal to `amount`: Answer is 1.
- Coin denominations larger than `amount`: Those coins are simply skipped.
