# Number of Substrings Containing All Three Characters (LC 1358)

Given a string `s` of only `'a'`, `'b'`, `'c'`, return the number of substrings
containing at least one of each character.

## Approaches

### 1. Sliding Window — O(n) time, O(1) space
For each `right`, find the smallest `left` such that the window `[left, right]` contains all three characters. Every extension of that window to the left (indices `0` to `left-1`) also forms a valid substring ending at `right`. Add `left` to the result.

**Why it works:** Once the window `[left, right]` is valid, any window `[0..left-1, right]` is also valid (it's a superset). So there are exactly `left` valid starting positions for each `right`.

## Key Insight
For each `right`, shrink the window until it's the smallest valid window. The number of valid substrings ending at `right` is exactly `left` (all starting positions from 0 to left-1).

## Edge Cases
- String length < 3 → 0 (can't contain all three)
- All characters the same → 0
- Exactly one of each character → 1
- String is `"abc"` repeated → many valid substrings
