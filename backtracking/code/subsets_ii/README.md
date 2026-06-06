# Subsets II (LC 90)

Given an integer array that may contain duplicates, return all possible unique subsets
(the power set). No duplicate subsets in the result.

## Approaches

### 1. Backtracking with Duplicate Skipping
**Complexity:** O(2ⁿ) time, O(n) space

Sort the array so duplicates are adjacent. Backtrack: at each level, skip an element
if it equals the previous element at the same recursion depth
(`i > start && nums[i] == nums[i-1]`). Add the current path to results at every node.

**Why it works:** Sorting groups duplicates. The skip condition prevents choosing the
same value twice at the same level, which would produce duplicate subsets. Unlike
Combination Sum II, we add to results at every step (not just at leaves) since we want
all subset sizes.

## Key Insight

The same duplicate-skipping pattern as Combination Sum II, but applied to subset
generation. Adding `current[:]` to results at every recursive call (not just base case)
generates all subset sizes simultaneously.

## Edge Cases

- All elements identical — subsets are `[], [x], [x,x], ..., [x,x,...,x]`.
- Single element — return `[[], [element]]`.
- No duplicates — same as Subsets (LC 78).
- Negative numbers — sorting still works; duplicates are still adjacent.
