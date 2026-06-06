# LC 139 — Word Break

Given a string `s` and a dictionary `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words. Words may be reused.

## Approaches

### 1. Top-down Memoization
- **Time:** O(n² × m) | **Space:** O(n)
- `dp(i)` = can `s[i:]` be segmented? Try all words starting at position `i`. If `s[i:j]` is in the dictionary and `dp(j)` is true, return true.

### 2. Bottom-up DP
- **Time:** O(n² × m) | **Space:** O(n)
- `dp[i] = True` if `s[:i]` can be segmented. For each `i`, check all `j < i` where `dp[j]` is true and `s[j:i]` is in the dictionary.

## Key Insight

The problem has optimal substructure: if `s[:j]` is segmentable and `s[j:i]` is a valid word, then `s[:i]` is segmentable. Using a hash set for the dictionary makes each word lookup O(1), reducing the per-position cost to O(n) word checks rather than O(n × max_word_length).

## Edge Cases

- Empty string: Trivially segmentable (base case `dp[0] = True`).
- Word not in dictionary at all: Return `False`.
- Same word repeated (e.g., `"aaa"` with `["a"]`): Works because words can be reused.
- Long string with no valid segmentation: DP correctly returns `False`.
