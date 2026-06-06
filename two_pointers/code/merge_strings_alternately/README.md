# Merge Strings Alternately (LC 1768)

Given two strings `word1` and `word2`, merge them by alternating characters starting
with `word1`. Append the remaining characters of the longer string at the end.

## Approaches

### 1. Index-Based Loop — O(n+m) time, O(n+m) space
Iterate up to `max(len(word1), len(word2))`. Conditionally append from each string.

**Why it works:** A single index covers both strings; bounds checks handle unequal lengths.

### 2. Two Pointers — O(n+m) time, O(n+m) space
Advance both pointers together while both strings have characters. Append the remaining tail of the longer string.

**Why it works:** Explicit two-pointer logic makes the alternating pattern clear. Appending the tail in one slice operation handles the unequal-length case cleanly.

## Key Insight
Both approaches are equivalent. The two-pointer version is more explicit about the alternating logic and the tail-append step.

## Edge Cases
- Equal length strings → perfectly interleaved, no tail
- One string much longer than the other → long tail appended
- Single-character strings
- One empty string → return the other string unchanged
