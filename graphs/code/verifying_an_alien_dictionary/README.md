# Verifying an Alien Dictionary (LC 953)

Given `words` and an alien alphabet `order`, return `true` if the words are sorted
lexicographically according to the alien alphabet.

## Approaches

### 1. Custom Rank Comparison
**Complexity:** O(n · m) time, O(1) space (n = words, m = max word length)

Build a rank map from the alien alphabet. Compare each adjacent pair of words
character by character using alien ranks. Return `false` on the first violation.

**Why it works:** Lexicographic order is determined by the first differing character.
If `words[i][j]` has higher rank than `words[i+1][j]`, the order is violated.
If `words[i]` is a prefix of `words[i+1]` but longer, it's also a violation.

## Key Insight

The only difference from standard lexicographic comparison is the character ordering.
Replacing the default ASCII order with the alien rank map makes this a direct
application of standard string comparison logic.

## Edge Cases

- `words[i]` is a prefix of `words[i+1]` but longer (e.g., `"apple"` before `"app"`) — `false`.
- Equal adjacent words — valid (equal is fine in sorted order).
- Single word — trivially sorted, return `true`.
- All words identical — return `true`.
