# Valid Palindrome II (LC 680)

Given a string `s`, return `true` if it can become a palindrome by deleting
at most one character.

## Approaches

### 1. Brute Force — O(n²) time
Try removing each character one at a time and check if the result is a palindrome.

**Why it works:** Exhaustive — tries all n possible deletions. O(n) per palindrome check × n deletions = O(n²).

### 2. Two Pointers with One Skip — O(n) time, O(1) space
Walk inward with two pointers. On the first mismatch, try skipping either the left or right character and check if the remaining substring is a palindrome.

**Why it works:** A valid one-deletion palindrome has at most one mismatch point. When found, exactly one of the two skip options must produce a palindrome — checking both covers all cases.

## Key Insight
Walk until the first mismatch, then try skipping left or right. Only one mismatch is allowed, so this single branch covers all valid cases in O(n).

## Edge Cases
- Already a palindrome → `true` (zero deletions needed)
- Single character → `true`
- Two different characters → `true` (delete either one)
- Multiple mismatches → `false`
- `"deeee"` → delete first `e` or last `e` to get palindrome
