# Combination Sum (LC 39)

Given distinct candidates and a target, find all unique combinations where candidates
sum to target. Each candidate may be used **unlimited times**.

## Approaches

### 1. Backtracking with Reuse
**Complexity:** O(n^(t/m)) time where t=target, m=min candidate; O(t/m) space

Sort candidates. Backtrack from `start`: for each candidate, subtract from remaining
and recurse with the **same index** `i` (allowing reuse). Prune when candidate exceeds
remaining. Record when remaining reaches 0.

**Why it works:** Recursing with `i` (not `i+1`) allows reusing the same candidate.
Starting from `start` (not 0) prevents duplicate combinations by enforcing that
combinations are non-decreasing. Sorting enables early termination when a candidate
exceeds the remaining target.

## Key Insight

The key difference from Combination Sum II: recurse with `i` instead of `i+1` to allow
reuse. The `start` parameter still prevents duplicates by ensuring we never go back to
earlier candidates.

## Edge Cases

- No combination sums to target — return `[]`.
- Single candidate equals target — return `[[candidate]]`.
- Target smaller than all candidates — return `[]`.
- Large target with small candidates — many combinations possible.
