# Combinations (LC 77)

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen
from the range `[1, n]`.

## Approaches

### 1. Backtracking with Pruning
**Complexity:** O(C(n,k) · k) time, O(k) space

Backtrack from `start` to `n`. At each step, add a number to the current combination
and recurse with `start+1`. Prune: if fewer than `k - len(current)` numbers remain in
`[start, n]`, stop early.

**Why it works:** Starting from `start` (not 1) avoids duplicate combinations. The
pruning condition `range(start, n - (k - len(current)) + 2)` ensures we only recurse
when enough numbers remain to complete a combination of size `k`.

## Key Insight

The pruning bound is the key optimization: we need at least `k - len(current)` more
numbers, so the loop only runs while `i ≤ n - (k - len(current))`. This cuts the
search space significantly for large `n` and small `k`.

## Edge Cases

- `k == n` — only one combination: `[1, 2, ..., n]`.
- `k == 1` — return `[[1], [2], ..., [n]]`.
- `k == 0` — return `[[]]` (empty combination).
- `n == 1, k == 1` — return `[[1]]`.
