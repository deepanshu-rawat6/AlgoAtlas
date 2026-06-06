# LC 279 — Perfect Squares

Given an integer `n`, return the least number of perfect square numbers (1, 4, 9, 16, ...) that sum to `n`.

## Approaches

### 1. DP
- **Time:** O(n × √n) | **Space:** O(n)
- `dp[i] = min(dp[i - sq] + 1)` for all perfect squares `sq <= i`. Initialize `dp[0] = 0`, rest to infinity. Build up from 1 to n.

### 2. BFS (Level = Number of Squares Used)
- **Time:** O(n × √n) | **Space:** O(n)
- Model as a shortest-path problem: nodes are integers, edges connect `x` to `x - sq` for each perfect square. BFS level = number of squares used. First time we reach 0 is the answer.

## Key Insight

This is equivalent to Coin Change where the "coins" are perfect squares. The DP recurrence `dp[i] = 1 + min(dp[i - sq])` works because using one perfect square reduces the problem to a smaller subproblem. BFS is natural here because all edges have weight 1 (each square counts as one step).

## Edge Cases

- `n = 1`: Answer is 1 (just 1²).
- Perfect square input (e.g., `n = 4`): Answer is 1.
- `n = 12 = 4 + 4 + 4`: Answer is 3.
- Lagrange's four-square theorem guarantees the answer is always ≤ 4.
