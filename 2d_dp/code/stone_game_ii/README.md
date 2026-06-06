# LC 1140 — Stone Game II

Alice and Bob take turns (Alice first). On each turn, a player takes the first `X` piles where `1 ≤ X ≤ 2M`, then `M = max(M, X)`. Initially `M = 1`. Return the maximum stones Alice can get.

## Approaches

### 1. Top-down Memoization with Suffix Sums
- **Time:** O(n³) | **Space:** O(n²)
- `dp(i, M)` = max stones current player can get from `piles[i:]` with current `M`. If `i + 2M >= n`, take all remaining. Otherwise: `suffix[i] - min(dp(i+x, max(M, x)) for x in 1..2M)`. Minimizing opponent's gain maximizes your own.

## Key Insight

The key insight is `dp(i, M) = suffix[i] - min(dp(i+x, max(M, x)))`. Since the total from position `i` is fixed (`suffix[i]`), maximizing your own score is equivalent to minimizing the opponent's score. Precomputing suffix sums avoids recomputing pile totals. The state space is O(n²) since `M` can grow up to `n`.

## Edge Cases

- Single pile: Alice takes it all (M=1, can take 1 pile).
- `i + 2M >= n`: Current player takes all remaining piles (greedy — no reason to leave anything).
- Large `M` relative to remaining piles: Same as above, take everything.
