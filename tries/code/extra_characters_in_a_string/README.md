# Extra Characters in a String (LC 2707)

Given string `s` and a dictionary, break `s` into substrings from the dictionary. Return the minimum number of characters left over (not covered by any dictionary word).

## Approaches

### DP + Hash Set
- **Time:** O(n² * m) where n = len(s), m = avg word length for hashing
- **Space:** O(n + dict size)
- `dp[i]` = min extra characters in `s[:i]`. Base: `dp[0] = 0`.
- For each position `i`, default is `dp[i-1] + 1` (skip character `s[i-1]` as extra).
- Then try every dictionary word ending at `i`: if `s[i-len(w):i] == w`, update `dp[i] = min(dp[i], dp[i-len(w)])`.

### DP + Trie
- **Time:** O(n² * m) with better constant — trie avoids re-hashing substrings
- **Space:** O(n + total trie characters)
- Same DP recurrence, but instead of checking every word at each position, walk the trie backwards from position `i` to find all matching words efficiently.

## Key Insight

This is a classic interval DP / word break variant. The key observation: `dp[i]` only improves when a dictionary word exactly covers `s[j:i]` — in that case we inherit `dp[j]` with zero extra characters for that segment. The trie version avoids redundant string comparisons by sharing prefix structure across dictionary words.

## Edge Cases

- No dictionary word matches any part of `s` → answer is `len(s)`.
- A dictionary word matches the entire string → answer is `0`.
- Overlapping matches: e.g., `s = "leetscode"`, both `"leet"` and `"leetcode"` match — DP naturally picks the better split.
- Dictionary words longer than `s` are simply never matched.
