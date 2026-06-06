# Minimum Window Subsequence (LC 727)

Given strings `s1` and `s2`, return the minimum window in `s1` such that `s2` is a
subsequence of that window. Return `""` if no such window exists.

## Approaches

### 1. Forward + Backward Two Pointers — O(n·m) time, O(1) space
Forward pass: scan `s1` left-to-right matching `s2` characters in order to find a window end.
Backward pass: from the window end, scan right-to-left matching `s2` in reverse to find the tightest window start.
Restart from `start + 1` to find the next candidate.

**Why it works:** The forward pass finds any valid window; the backward pass tightens it to the minimum. Restarting from `start + 1` ensures all candidates are explored.

### 2. DP — O(n·m) time, O(m) space
`dp[j]` = earliest start index in `s1` to match `s2[:j]` ending at the current `s1` position.

**Why it works:** Tracks the best starting position for each prefix of `s2` matched so far.

## Key Insight
Forward scan finds a valid window; backward scan from its end finds the tightest left boundary. This two-phase approach avoids re-scanning from scratch.

## Edge Cases
- `s2` not a subsequence of `s1` → return `""`
- `s2` longer than `s1` → return `""`
- Multiple valid windows → return the shortest
- `s2` is a single character → shortest window is that character's first occurrence
