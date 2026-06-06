# Permutations (LC 46)

Given an array of **distinct** integers, return all possible permutations.

## Approaches

### 1. Backtracking with Used Array
**Complexity:** O(n!) time, O(n) space

Use a `used` boolean array. For each position, try all unused elements. Mark as used
before recursing; unmark on backtrack. Add to results when path length equals `n`.

**Why it works:** Each permutation is a unique ordering of all elements. The `used`
array ensures each element appears exactly once per permutation. Backtracking explores
all n! orderings.

### 2. Swap-Based Backtracking
**Complexity:** O(n!) time, O(n) space

Swap element at current index with each element from current index to end. Recurse
with `start+1`. Swap back to restore.

**Why it works:** Swapping fixes one element at each position and recursively permutes
the rest. Swapping back restores the array for the next iteration.

## Key Insight

Permutations differ from combinations in that order matters. The `used` array (or swap
approach) ensures all n! orderings are generated. Unlike combinations, there's no
`start` parameter — every unused element is a valid choice at each position.

## Edge Cases

- Single element — return `[[element]]`.
- Two elements — return `[[a,b],[b,a]]`.
- `n = 8` (max) — 40,320 permutations.
