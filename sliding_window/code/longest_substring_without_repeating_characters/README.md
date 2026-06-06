# Longest Substring Without Repeating Characters (LC 3)

Given a string `s`, find the length of the longest substring without repeating characters.

## Approaches

### 1. Brute Force — O(n³) time, O(min(n,m)) space
Try all substrings; check uniqueness via a set for each.

**Why it works:** Correct but checks redundant substrings.

### 2. Sliding Window with Last-Seen Index — O(n) time, O(min(n,m)) space
Maintain a `char → last_index` map. For each character, if it was seen within the current window, jump `left` past its last occurrence. Update the character's index and track the best window size.

**Why it works:** When a duplicate is found, the window's left boundary must move past the previous occurrence of that character. Storing the last index allows jumping directly instead of shrinking one step at a time.

## Key Insight
Jump `left` directly to `last_seen[char] + 1` when a duplicate is found — avoids O(n) shrinking per duplicate.

## Edge Cases
- Empty string → 0
- All identical characters → 1
- All unique characters → length of string
- Characters outside lowercase letters (digits, symbols, spaces — all valid)
