# Count Different Palindromic Subsequences — LC 730

## Problem

Given string `s` containing only `a`, `b`, `c`, `d`, count the number of **distinct** non-empty palindromic subsequences. Return the answer mod 10^9 + 7.

**Example:** `s="bccb"` → 6 (`"b"`, `"c"`, `"bb"`, `"cc"`, `"bcb"`, `"bccb"`)

## Approach: Interval DP

**Why interval DP?** Palindromes have recursive structure: a palindrome of length > 2 has a palindrome at its core. `dp[i][j]` = distinct palindromic subsequences in `s[i..j]`.

**Recurrence:** For each character `c` in `{a,b,c,d}`:
- Find `lo` = first occurrence of `c` in `[i,j]`
- Find `hi` = last occurrence of `c` in `[i,j]`
- **No `c`:** add 0
- **One `c` (lo == hi):** add 1 (just `"c"`)
- **Two adjacent `c`s (lo+1 == hi):** add 2 (`"c"` and `"cc"`)
- **Two `c`s with gap:** add `dp[lo+1][hi-1] + 2`
  - `dp[lo+1][hi-1]`: each inner palindrome wrapped by `c` → new distinct palindrome
  - `+2`: `"c"` and `"cc"` themselves

**Optimization:** Precompute `next_occ[i][c]` and `prev_occ[i][c]` for O(1) lo/hi lookup → total O(n²).

**Complexity:** O(n²) time and space

## Key Insight

The `+2` accounts for `"c"` and `"cc"`. The `dp[lo+1][hi-1]` term counts all distinct palindromes in the inner range, each of which becomes a new distinct palindrome when wrapped by `c`.

## Edge Cases

- Single character → 1
- All same characters (e.g., `"aaaa"`) → 4 (`"a"`, `"aa"`, `"aaa"`, `"aaaa"`)
- No repeated characters → only single-char palindromes
- Answer must be taken mod 10^9 + 7
