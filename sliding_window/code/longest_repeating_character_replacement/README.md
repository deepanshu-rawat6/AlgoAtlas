# Longest Repeating Character Replacement (LC 424)

Given a string `s` and integer `k`, you can change at most `k` characters to any letter.
Return the length of the longest substring containing the same letter after at most `k` changes.

## Approaches

### 1. Brute Force — O(n²) time, O(1) space
Try all windows; a window is valid if `(window_size - max_freq) <= k`.

**Why it works:** Correct but checks every possible window.

### 2. Sliding Window — O(n) time, O(1) space
Expand right always. Track `max_freq` (highest frequency of any character in the window). If `window_size - max_freq > k`, slide left by 1. `max_freq` only ever increases — we only care about windows larger than the current best.

**Why it works:** `window_size - max_freq` = number of characters that need to be replaced. When this exceeds `k`, the window is invalid. We slide (not reset) because we only want windows larger than what we've seen.

## Key Insight
`window_size - max_freq <= k` is the validity condition. `max_freq` never decreases — we slide the window rather than shrink it, since smaller windows can't improve the answer.

## Edge Cases
- `k == 0` → longest run of identical characters
- `k >= len(s)` → entire string is valid
- Single character string → 1
- All characters identical → entire string
