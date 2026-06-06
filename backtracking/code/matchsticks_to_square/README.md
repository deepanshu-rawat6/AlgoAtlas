# Matchsticks to Square (LC 473)

Given matchstick lengths, determine if they can form a square using all sticks exactly once.

## Approaches

### 1. Backtracking with Pruning
**Complexity:** O(4ⁿ) time, O(n) space

Check total sum divisible by 4; each side = sum/4. Sort descending for better pruning.
Try assigning each matchstick to one of 4 sides. Prune if a side would exceed the target.
Skip symmetric branches: if a side is empty and we fail, no need to try other empty sides.

**Why it works:** We try all assignments of sticks to 4 buckets. Sorting descending
places large sticks first, failing fast when a stick is too long. The symmetry pruning
(`if sides[i] == 0: break`) avoids redundant exploration of equivalent empty buckets.

## Key Insight

This is the **partition into k equal subsets** problem with k=4. The key optimizations:
1. Sort descending — large sticks fail fast.
2. Skip empty buckets after first failure — all empty buckets are equivalent.
3. Early termination if any stick > side length.

## Edge Cases

- Total sum not divisible by 4 — return `false` immediately.
- Any single stick longer than `sum/4` — return `false` immediately.
- All sticks equal — return `true` if count divisible by 4.
- Single stick — return `false` (can't form a square with one stick).
