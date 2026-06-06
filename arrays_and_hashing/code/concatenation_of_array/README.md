# Concatenation of Array (LC 1929)

Given an integer array `nums` of length `n`, return an array of length `2n` that is
`nums` concatenated with itself: `ans[i] == nums[i]` and `ans[i+n] == nums[i]`.

## Approaches

### 1. Loop — O(n) time, O(n) space
Append all elements twice using a loop.

**Why it works:** Straightforward iteration builds the result by appending each element from `nums` twice.

### 2. List Concatenation — O(n) time, O(n) space
Return `nums + nums` directly.

**Why it works:** Python's `+` operator on lists creates a new list containing all elements of both operands — a one-liner that expresses the intent directly.

## Key Insight
`nums + nums` is the most direct expression of the problem. Both approaches are O(n); the built-in is cleaner.

## Edge Cases
- Single-element array → `[x, x]`
- All elements identical → doubled array of same value
- Large `n` (up to 1000) → output size up to 2000, well within memory
