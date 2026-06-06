# LC 97 — Interleaving String

Given strings `s1`, `s2`, and `s3`, determine if `s3` is formed by interleaving `s1` and `s2` while preserving the relative order of characters from each.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- `dp[i][j]` = can `s1[:i]` and `s2[:j]` interleave to form `s3[:i+j]`. Transition: `(dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])`.

### 2. 1D DP (Space-Optimized)
- **Time:** O(m × n) | **Space:** O(n)
- Roll the 2D table row by row. `dp[j]` represents `dp[i][j]` for the current row `i`.

## Key Insight

At each position in `s3`, the character must come from either `s1` or `s2` (maintaining relative order). The 2D DP state `dp[i][j]` captures whether we've successfully consumed `i` characters from `s1` and `j` from `s2`. The first check `len(s1) + len(s2) != len(s3)` is a critical early exit.

## Edge Cases

- Both `s1` and `s2` empty: `s3` must also be empty.
- One string empty: `s3` must equal the other string.
- `len(s1) + len(s2) != len(s3)`: Immediately return `False`.
- Duplicate characters across `s1` and `s2`: The DP correctly tracks which source each character came from.
