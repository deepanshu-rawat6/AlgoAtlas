# Permutations II (LC 47)

Given a collection of numbers that may contain duplicates, return all unique permutations.

## Approaches

### 1. Backtracking with Used Array and Duplicate Skipping
**Complexity:** O(n!) time, O(n) space

Sort the array. Use a `used` boolean array. For each position, skip if:
1. `used[i]` is `True` (already in current permutation), or
2. `nums[i] == nums[i-1]` and `not used[i-1]` (duplicate at same level).

**Why it works:** Sorting groups duplicates. The condition `nums[i] == nums[i-1] and not used[i-1]`
ensures that among duplicate values, we always pick the leftmost one first at each
recursion level. This generates each unique permutation exactly once.

## Key Insight

The duplicate-skipping condition is subtle: `not used[i-1]` means the previous identical
element was **not** used in the current path (it was skipped at this level). This enforces
a canonical ordering: among duplicates, always pick the first available one, preventing
the same permutation from being generated via different orderings of identical elements.

## Edge Cases

- All elements identical — only one unique permutation: `[x, x, ..., x]`.
- No duplicates — same as Permutations (LC 46), generates n! permutations.
- Two identical elements — generates n!/2! unique permutations.
- Negative numbers — sorting still works correctly.
