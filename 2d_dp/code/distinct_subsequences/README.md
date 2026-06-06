# LC 115 — Distinct Subsequences

Given strings `s` and `t`, return the number of distinct subsequences of `s` that equal `t`.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- `dp[i][j]` = ways to form `t[:j]` from `s[:i]`. If `s[i-1] == t[j-1]`: `dp[i-1][j-1] + dp[i-1][j]` (use or skip the match). Otherwise: `dp[i-1][j]` (skip `s[i-1]`).

### 2. 1D DP (Space-Optimized)
- **Time:** O(m × n) | **Space:** O(n)
- Iterate backwards over `t` for each character in `s`. When `s[i] == t[j]`, add `dp[j-1]` to `dp[j]`. Backward iteration prevents using the same `s[i]` twice.

## Key Insight

At each matching character pair `s[i] == t[j]`, you have two choices: use this match (contributing `dp[i-1][j-1]` ways) or skip `s[i]` and find `t[j]` later (contributing `dp[i-1][j]` ways). The backward iteration in the 1D version is essential — it ensures `dp[j-1]` still reflects the state before processing `s[i]`.

## Edge Cases

- `t` is empty: One way (empty subsequence). `dp[i][0] = 1` for all `i`.
- `s` is shorter than `t`: Impossible, return 0.
- `s == t`: Exactly one way.
- Repeated characters in `s` (e.g., `"rabbbit"` → `"rabbit"`): Each repeated character contributes independently.
