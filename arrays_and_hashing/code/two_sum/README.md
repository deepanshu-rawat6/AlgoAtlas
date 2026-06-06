# Two Sum (LC 1)

Given an array `nums` and an integer `target`, return the indices of the two numbers
that add up to `target`. Exactly one solution exists; you may not use the same element twice.

## Approaches

### 1. Brute Force — O(n²) time, O(1) space
Check every pair `(i, j)` until their sum equals `target`.

**Why it works:** Exhaustive search guarantees finding the pair, but checks redundant combinations.

### 2. Hash Map — O(n) time, O(n) space
For each number, compute `complement = target - num`. If complement is already in the map, return both indices. Otherwise store `num → index`.

**Why it works:** Each number has exactly one complement. Storing seen numbers lets us find the complement in O(1) instead of scanning again.

## Key Insight
Trade space for time: one pass with a hash map turns an O(n) inner scan into O(1) lookup.

## Edge Cases
- Duplicate values used at different indices (e.g., `[3,3]`, target=6)
- Negative numbers
- Exactly one solution guaranteed — no need to handle zero solutions
