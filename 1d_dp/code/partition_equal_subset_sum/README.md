# LC 416 — Partition Equal Subset Sum

Given an integer array `nums`, return `true` if you can partition it into two subsets with equal sum.

## Approaches

### 1. Top-down Memoization
- **Time:** O(n × sum) | **Space:** O(n × sum)
- Reduce to subset sum: can any subset sum to `total / 2`? `dp(i, rem)` tries including or excluding `nums[i]`.

### 2. Bottom-up DP (Boolean Set)
- **Time:** O(n × sum) | **Space:** O(sum)
- Maintain a set of reachable sums. For each number, add it to every existing reachable sum. Check if `target` is reachable.

### 3. Bitset Optimization
- **Time:** O(n × sum / 64) | **Space:** O(sum / 64)
- Represent reachable sums as bits in an integer. `bits |= bits << num` shifts all reachable sums by `num` in one operation. Check bit at position `target`.

## Key Insight

Equal partition exists iff some subset sums to `total / 2`. This reduces a 2D partition problem to a 1D subset-sum problem. If `total` is odd, immediately return `False`. The bitset trick is the most elegant: shifting a bitmask by `num` simultaneously adds `num` to all currently reachable sums.

## Edge Cases

- Odd total sum: Impossible, return `False`.
- Single element equal to `total / 2`: Impossible (need at least 2 elements).
- All elements equal: Possible only if count is even.
- One element larger than `total / 2`: Impossible.
