# LC 1143 — Longest Common Subsequence

Given two strings `text1` and `text2`, return the length of their longest common subsequence (LCS). A subsequence preserves relative order but need not be contiguous.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- `dp[i][j]` = LCS of `text1[:i]` and `text2[:j]`. If characters match: `dp[i-1][j-1] + 1`. Otherwise: `max(dp[i-1][j], dp[i][j-1])`.

### 2. 1D DP (Space-Optimized)
- **Time:** O(m × n) | **Space:** O(min(m, n))
- Keep one row and a `prev` variable for the diagonal. Roll row by row, tracking the previous diagonal value to simulate `dp[i-1][j-1]`.

## Key Insight

When characters match, the LCS extends by 1 from the diagonal (both strings advance). When they don't match, the LCS is the best of skipping one character from either string. The diagonal dependency is why the 1D optimization needs a `prev` variable — the current `dp[j]` before update represents `dp[i-1][j]`, and `prev` holds `dp[i-1][j-1]`.

## Edge Cases

- Either string empty: LCS is 0.
- Identical strings: LCS equals the string length.
- No common characters: LCS is 0.
- One string is a subsequence of the other: LCS equals the shorter string's length.
