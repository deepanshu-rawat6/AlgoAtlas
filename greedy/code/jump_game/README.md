# LC 55 — Jump Game

Given `nums[i]` as the maximum jump length from index `i`, return `true` if you can reach the last index starting from index 0.

## Approaches

### 1. DP
- **Time:** O(n²) | **Space:** O(n)
- `dp[i] = True` if index `i` is reachable. For each reachable `j`, mark all `j + nums[j]` positions as reachable.

### 2. Greedy (Track Farthest Reachable)
- **Time:** O(n) | **Space:** O(1)
- Track `farthest` = the farthest index reachable so far. At each index `i`, if `i > farthest`, we're stuck — return `False`. Otherwise update `farthest = max(farthest, i + nums[i])`.

## Key Insight

We don't need to track which specific jumps to take — only whether the current index is reachable. If `i > farthest`, there's a gap we can't cross. The greedy approach works because if we can reach index `i`, we can reach any index up to `i + nums[i]`, so tracking the maximum reachable index is sufficient.

## Edge Cases

- Single element: Already at the last index, return `True`.
- `nums[0] = 0` and `n > 1`: Stuck at index 0, return `False`.
- All zeros except last: Return `False` unless `n = 1`.
- Large jumps early: `farthest` quickly covers the entire array.
