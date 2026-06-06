# LC 746 — Min Cost Climbing Stairs

Given `cost[i]` as the cost of the i-th step, you can start from index 0 or 1 and climb 1 or 2 steps at a time. Return the minimum cost to reach the top (beyond the last index).

## Approaches

### 1. Top-down Memoization
- **Time:** O(n) | **Space:** O(n)
- `dp(i) = cost[i] + min(dp(i+1), dp(i+2))`. The top is reached when `i >= n`, returning 0. Start with `min(dp(0), dp(1))`.

### 2. Bottom-up DP
- **Time:** O(n) | **Space:** O(n)
- `dp[i]` = min cost to reach step `i`. `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`. The "top" is index `n`.

### 3. Space-Optimized
- **Time:** O(n) | **Space:** O(1)
- Roll two variables `a, b` representing the cost to reach the previous two positions.

## Key Insight

The "top" is one step beyond the last index. You can reach it from either the last or second-to-last step. The DP models the cost to reach each position, not the cost at each position — paying `cost[i]` only when you step on it, then choosing the cheaper of the two possible next steps.

## Edge Cases

- Two steps: `min(cost[0], cost[1])` — pick the cheaper starting step.
- All zeros: Return 0.
- Can start at index 0 or 1, so the answer is `min(dp(0), dp(1))`.
