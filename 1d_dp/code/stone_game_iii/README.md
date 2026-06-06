# LC 1406 — Stone Game III

Alice and Bob take turns (Alice first). Each turn, a player takes 1, 2, or 3 stones from the front. The player with the most stones wins. Both play optimally. Return "Alice", "Bob", or "Tie".

## Approaches

### 1. Top-down Memoization
- **Time:** O(n) | **Space:** O(n)
- `dp(i)` = max score **advantage** (current player's score minus opponent's) from index `i`. Try taking 1, 2, or 3 stones; subtract opponent's optimal play from the remaining pile.

### 2. Bottom-up DP
- **Time:** O(n) | **Space:** O(n)
- Build from the end. `dp[i] = max over k in [1,3] of (sum of k stones - dp[i+k])`. The subtraction models the zero-sum nature: what the opponent gains is what you lose.

## Key Insight

The key is modeling the game as a **score difference** rather than absolute scores. `dp(i) = total_taken - opponent_optimal` captures the net advantage. A positive result means the current player wins. The subtraction `total - dp(i+k)` works because the opponent faces the same optimization from position `i+k`.

## Edge Cases

- All negative values: The player forced to take stones loses; the DP handles this correctly.
- Single stone: Alice takes it; if positive she wins, if negative Bob wins (Alice is forced).
- `dp(i) == 0`: Tie — both players end with equal scores.
