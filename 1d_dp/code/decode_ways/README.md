# LC 91 — Decode Ways

A message of letters A–Z is encoded as "1"–"26". Given a digit string `s`, return the number of ways to decode it. Leading zeros and invalid two-digit codes (> 26) have zero decodings.

## Approaches

### 1. Top-down Memoization
- **Time:** O(n) | **Space:** O(n)
- `dp(i)` = ways to decode `s[i:]`. If `s[i] == '0'`, return 0. Otherwise add `dp(i+1)` (single digit) and `dp(i+2)` if `s[i:i+2]` is in `[10, 26]`.

### 2. Bottom-up DP
- **Time:** O(n) | **Space:** O(n)
- Build from the end. `dp[n] = 1` (empty suffix). For each `i`, `dp[i] = dp[i+1]` if non-zero, plus `dp[i+2]` if two-digit is valid.

### 3. Space-Optimized
- **Time:** O(n) | **Space:** O(1)
- Keep only `next1` (dp[i+1]) and `next2` (dp[i+2]) as rolling variables.

## Key Insight

Each position can decode as a single digit (always valid if non-zero) or as a two-digit number with the next character (valid if the pair is 10–26). A `'0'` digit can never start a valid single-digit decode, so it contributes 0 ways on its own — it must be part of a valid two-digit code (10 or 20).

## Edge Cases

- String starting with `'0'`: Return 0.
- `"10"` or `"20"`: Only one way (the two-digit decode).
- `"30"` through `"90"`: The `'0'` can't be decoded alone and the pair > 26, so return 0.
- Single character `"0"`: Return 0.
