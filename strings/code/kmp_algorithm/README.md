# KMP Algorithm — LC 28

## Problem

Find the first occurrence of `pattern` in `text` using KMP. Return -1 if not found.

**Example:** `text="AABAACAADAABAABA"`, `pattern="AABA"` → 0

## Approach: LPS Array + Matching

**Why LPS?** Naive matching restarts from 0 on every mismatch → O(nm). KMP avoids this by precomputing how much of the pattern can be "reused" after a mismatch.

**LPS[i]** = length of longest proper prefix of `pattern[0..i]` that is also a suffix.

**Build LPS — O(m):**
- Two pointers: `length` (prev longest prefix-suffix) and `i`
- Match: `lps[i] = ++length`, advance `i`
- Mismatch with `length > 0`: `length = lps[length-1]` (key step — don't reset to 0)
- Mismatch with `length == 0`: `lps[i] = 0`, advance `i`

**Search — O(n):**
- On mismatch at `pattern[j]`: jump to `j = lps[j-1]` instead of `j = 0`
- On `j == m`: found at `i - m`

**Complexity:** O(n+m) time, O(m) space

## Key Insight

`lps[j-1]` tells us: "the first `lps[j-1]` characters of the pattern already match the text at this position." We skip re-checking them.

## Edge Cases

- Empty pattern → return 0
- Pattern longer than text → return -1
- All same characters (e.g., `"aaaa"` in `"aaaaa"`) → LPS = [0,1,2,3], works correctly
