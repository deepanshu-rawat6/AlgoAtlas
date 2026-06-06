# LC 72 — Edit Distance

Given two strings `word1` and `word2`, return the minimum number of operations (insert, delete, replace) to convert `word1` to `word2`.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- `dp[i][j]` = min edits to convert `word1[:i]` to `word2[:j]`. If characters match: `dp[i-1][j-1]`. Otherwise: `1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])` for replace, delete, insert.

### 2. 1D DP (Space-Optimized)
- **Time:** O(m × n) | **Space:** O(min(m, n))
- Keep one row and a `prev` variable for the diagonal. Roll the DP row by row, tracking the previous diagonal value explicitly.

## Key Insight

The three operations map directly to three DP transitions: replace uses the diagonal `dp[i-1][j-1]`, delete uses `dp[i-1][j]` (remove from word1), insert uses `dp[i][j-1]` (add to word1). The base cases `dp[i][0] = i` and `dp[0][j] = j` represent converting to/from an empty string using only deletions/insertions.

## Edge Cases

- Either string empty: Answer is the length of the other string.
- Identical strings: Answer is 0.
- Completely different strings: Answer is `max(m, n)` (replace all + insert/delete remainder).
- Single character difference: Answer is 1.
