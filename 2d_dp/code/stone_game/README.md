# LC 877 — Stone Game

Alice and Bob take turns (Alice first) picking the entire pile from either end of a row. The player with the most stones wins. Both play optimally. Return `true` if Alice wins.

## Approaches

### 1. Math (O(1))
- **Time:** O(1) | **Space:** O(1)
- Alice always wins. With an even number of piles and an odd total, Alice can always choose to take all even-indexed or all odd-indexed piles (whichever has more stones), since she goes first.

### 2. DP (for generality)
- **Time:** O(n²) | **Space:** O(n²)
- `dp[i][j]` = max score difference (current player minus opponent) for piles `[i..j]`. `dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])`. Positive result means current player wins.

## Key Insight

The math solution works because Alice has first-mover advantage with even piles: she can always guarantee taking the better of the two "color" groups (even-indexed vs odd-indexed piles). The DP approach is more general and works for variants where Alice doesn't always win. The score-difference formulation elegantly handles the zero-sum nature.

## Edge Cases

- Two piles: Alice takes the larger one.
- All equal piles: Alice wins by total > 0 (odd total guaranteed).
- The math solution only applies when piles count is even and total is odd (problem constraints).
