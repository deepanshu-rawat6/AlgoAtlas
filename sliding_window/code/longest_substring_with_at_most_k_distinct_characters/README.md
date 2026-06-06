# Longest Substring with At Most K Distinct Characters (LC 340)

Given a string `s` and integer `k`, return the length of the longest substring
containing at most `k` distinct characters.

## Approaches

### 1. Sliding Window — O(n) time, O(k) space
Maintain a frequency map of characters in the current window. Expand right always. When distinct character count exceeds `k`, shrink from the left until it's ≤ `k` again.

**Why it works:** The window always satisfies the at-most-k constraint. Shrinking removes the leftmost character and deletes it from the map when its count reaches zero, reducing the distinct count.

## Key Insight
Variable-size sliding window: expand greedily, shrink only when the constraint is violated. `len(freq_map)` gives the distinct count in O(1).

## Edge Cases
- `k == 0` → return 0 (no characters allowed)
- `k >= len(set(s))` → return `len(s)` (all characters fit)
- Single character string → 1
- All characters identical → `len(s)` for any `k >= 1`
- `k == 1` → longest run of a single character
