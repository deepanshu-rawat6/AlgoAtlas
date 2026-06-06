# Combination Sum II (LC 40)

Given candidates (may contain duplicates) and a target, find all unique combinations
that sum to target. Each candidate may be used **at most once**.

## Approaches

### 1. Backtracking with Duplicate Skipping
**Complexity:** O(2ⁿ) time, O(n) space

Sort candidates so duplicates are adjacent. Backtrack: for each position, skip if the
value equals the previous value at the same recursion level (`i > start && candidates[i] == candidates[i-1]`).
Recurse with `i+1` (each element used at most once).

**Why it works:** Sorting groups duplicates together. Skipping duplicate values at the
same level prevents generating duplicate combinations. Using `i+1` (not `i`) ensures
each element is used at most once.

## Key Insight

The duplicate-skipping condition `i > start && candidates[i] == candidates[i-1]` is
the core trick. It allows using the same value multiple times across different positions
(e.g., two `1`s from the input) but prevents generating the same combination twice by
skipping duplicate choices at the same recursion depth.

## Edge Cases

- No combination sums to target — return `[]`.
- Single element equals target — return `[[element]]`.
- Multiple identical elements — can use them all if their sum equals target.
- Target is 0 — return `[[]]` (empty combination).
