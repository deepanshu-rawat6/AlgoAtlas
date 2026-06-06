# LC 198 — House Robber

You are a robber planning to rob houses along a street. Adjacent houses have connected alarms — you cannot rob two adjacent houses. Given `nums[i]` as the money in each house, return the maximum amount you can rob.

## Approaches

### 1. Top-down Memoization
- **Time:** O(n) | **Space:** O(n)
- `dp(i) = max(nums[i] + dp(i+2), dp(i+1))`: at each house, choose to rob it (skip next) or skip it.

### 2. Bottom-up DP
- **Time:** O(n) | **Space:** O(n)
- `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. Base: `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`.

### 3. Space-Optimized (Two Variables)
- **Time:** O(n) | **Space:** O(1)
- Roll `prev2, prev1 = prev1, max(prev1, prev2 + num)`. Only the last two states matter.

## Key Insight

At each house you make a binary choice: rob it (gaining `nums[i]` but skipping `i+1`) or skip it. The optimal substructure means the best decision at house `i` only depends on the best outcomes from `i+1` and `i+2` — everything further is already captured in those values.

## Edge Cases

- Single house: Return `nums[0]`.
- Two houses: Return `max(nums[0], nums[1])`.
- All zeros: Return 0.
- Alternating high-low values: The DP naturally picks the optimal non-adjacent subset.
