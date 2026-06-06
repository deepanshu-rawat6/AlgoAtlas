# LC 518 — Coin Change II

Given coin denominations and an `amount`, return the number of **combinations** (unordered) that make up that amount. Each coin can be used unlimited times.

## Approaches

### 1. 2D DP
- **Time:** O(n × amount) | **Space:** O(n × amount)
- `dp[i][j]` = ways to make amount `j` using first `i` coins. Either skip coin `i` (`dp[i-1][j]`) or use it (`dp[i][j - coin]`).

### 2. 1D DP (Space-Optimized)
- **Time:** O(n × amount) | **Space:** O(amount)
- For each coin, iterate amounts from `coin` to `amount` and add `dp[j - coin]` to `dp[j]`. The forward iteration (not backward) allows reusing the same coin multiple times.

## Key Insight

The critical difference from Combination Sum IV: the outer loop is over **coins** and the inner loop over **amounts**. This ensures each coin is considered in order, preventing the same combination from being counted multiple times in different orders. Forward iteration within the inner loop enables unlimited coin reuse (unbounded knapsack).

## Edge Cases

- `amount = 0`: One way (empty combination). `dp[0] = 1`.
- No coin can reach `amount`: Return 0.
- Single coin equal to `amount`: Return 1.
- `coins = [2], amount = 3`: Impossible (odd amount with only even coin), return 0.
