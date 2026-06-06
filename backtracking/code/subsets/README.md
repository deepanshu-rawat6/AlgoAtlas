# Subsets (LC 78)

Given an array of **unique** integers, return all possible subsets (the power set).

## Approaches

### 1. Backtracking
**Complexity:** O(2ⁿ · n) time, O(n) space

Backtrack from `start`: add the current path to results, then for each index from
`start` to end, include that element and recurse with `start+1`.

**Why it works:** Adding to results at every node (not just leaves) generates all
subset sizes. Starting from `start` ensures each element is considered only once per
path, preventing duplicates.

### 2. Bitmask Enumeration
**Complexity:** O(2ⁿ · n) time, O(1) extra space

For each integer from 0 to 2ⁿ-1, the set bits indicate which elements to include.

**Why it works:** Each integer from 0 to 2ⁿ-1 uniquely represents one subset via its
binary representation.

## Key Insight

The power set has exactly 2ⁿ subsets. Backtracking generates them by making an
include/exclude decision for each element. The `start` parameter ensures we only
move forward, generating each subset exactly once.

## Edge Cases

- Empty array — return `[[]]` (only the empty subset).
- Single element — return `[[], [element]]`.
- All elements distinct (guaranteed) — exactly 2ⁿ subsets.
