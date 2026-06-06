# Combination Sum III (LC 216)

Find all combinations of `k` numbers from 1-9 that sum to `n`. Each number used at
most once; no repeated combinations.

## Approaches

### 1. Backtracking with Pruning
**Complexity:** O(C(9,k)) time, O(k) space

Backtrack over digits 1-9 starting from `start`. Add digit to current combination;
recurse with `start+1`. Record when `len(current) == k` and `remaining == 0`. Prune
when remaining < 0 or not enough digits left to reach `k`.

**Why it works:** The search space is small (digits 1-9, at most 9 choices). Starting
from `start` prevents duplicates. Pruning on `remaining < 0` and insufficient remaining
digits cuts the search tree significantly.

## Key Insight

The fixed digit range [1-9] and small `k` (≤ 9) make this tractable. The key pruning:
if `remaining < 0` or `len(current) + (9 - start + 1) < k`, there's no valid completion.
This is a constrained version of Combination Sum with a fixed pool of digits.

## Edge Cases

- `k = 1` — return `[[n]]` if `1 ≤ n ≤ 9`, else `[]`.
- `n` too large for `k` digits from 1-9 — return `[]` (max sum = 9+8+...+(10-k)).
- `n` too small for `k` digits — return `[]` (min sum = 1+2+...+k).
- `k = 9, n = 45` — only one combination: `[1,2,3,4,5,6,7,8,9]`.
