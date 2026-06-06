# Partition to K Equal Sum Subsets (LC 698)

Given an integer array `nums` and integer `k`, return `true` if it's possible to divide
`nums` into `k` non-empty subsets each with equal sum.

## Approaches

### 1. Backtracking with Bucket Pruning
**Complexity:** O(k^n) time, O(n) space

Check total sum divisible by `k`; target = sum/k. Sort descending for better pruning.
Try placing each number into one of `k` buckets. Prune if bucket would exceed target.
Skip duplicate bucket sums to avoid symmetric branches.

**Why it works:** We try all assignments of numbers to k buckets. Sorting descending
places large numbers first, failing fast. Skipping buckets with the same current sum
avoids exploring equivalent states (all empty buckets are interchangeable).

## Key Insight

This generalizes Matchsticks to Square (k=4). The critical pruning: after failing to
place a number in a bucket of sum `s`, skip all other buckets with the same sum `s` —
they'll fail identically. This dramatically reduces the search space.

## Edge Cases

- Total sum not divisible by `k` — return `false` immediately.
- Any element > target — return `false` immediately.
- `k = 1` — always `true` (one subset = entire array).
- `k = n` — `true` iff all elements are equal.
- All elements equal — `true` iff `n` divisible by `k`.
