# LC 377 — Combination Sum IV

Given an array of distinct integers `nums` and a target integer `target`, return the number of possible **ordered** combinations (permutations) that add up to `target`. The same number may be used multiple times.

## Approaches

### 1. Top-down Memoization
- **Time:** O(target × n) | **Space:** O(target)
- `dp(rem) = sum(dp(rem - num) for num in nums if num <= rem)`. Base case: `dp(0) = 1`. Order matters, so we try all numbers at every position.

### 2. Bottom-up DP
- **Time:** O(target × n) | **Space:** O(target)
- `dp[0] = 1`. For each amount `i` from 1 to target, add `dp[i - num]` for every valid `num`. The outer loop over amounts (not items) is what counts ordered sequences.

## Key Insight

Unlike Coin Change II (which counts unordered combinations), here the outer loop iterates over **amounts** and the inner loop over **numbers**. This allows the same number to appear in different positions, naturally counting all orderings. Swapping the loop order would give unordered combinations instead.

## Edge Cases

- `target = 0`: One way (empty combination). Return 1.
- All numbers larger than `target`: Return 0.
- `nums = [9], target = 3`: Impossible, return 0.
