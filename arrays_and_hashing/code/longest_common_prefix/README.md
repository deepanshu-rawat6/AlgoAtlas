# Longest Common Prefix (LC 14)

Find the longest common prefix string among an array of strings.
Return `""` if there is no common prefix.

## Approaches

### 1. Vertical Scan — O(S) time, O(1) space
Check each character position across all strings simultaneously. Stop when any string diverges or runs out.

**Why it works:** The common prefix ends at the first position where any string differs. Checking column by column finds this boundary directly.

### 2. Sort + Compare Extremes — O(n log n · m) time, O(1) space
Sort the array. The common prefix of the lexicographically smallest and largest strings is the common prefix of all strings.

**Why it works:** After sorting, the first and last strings are the most different. Any prefix shared by both extremes is shared by every string in between.

## Key Insight
After sorting, only compare the first and last strings — they represent the maximum divergence, so their common prefix is the answer for the whole array.

## Edge Cases
- Single string → the string itself is the prefix
- Empty string in the array → prefix is `""`
- No common prefix at all → `""`
- All strings identical → the full string is the prefix
