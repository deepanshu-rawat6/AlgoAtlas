# 4Sum (LC 18)

Given an array `nums` and integer `target`, return all unique quadruplets
`[a, b, c, d]` such that `a + b + c + d == target`.

## Approaches

### 1. Brute Force — O(n⁴) time, O(n) space
Try all quadruplets; use a set to deduplicate.

**Why it works:** Correct but impractical for large inputs.

### 2. Sort + Two Outer Loops + Two Pointers — O(n³) time, O(1) extra space
Sort the array. Fix two outer indices `i` and `j`, then use two pointers `lo` and `hi` for the remaining pair. Skip duplicates at each level.

**Why it works:** Reduces 4Sum to 3Sum, which reduces to Two Sum II. Each level of fixing an element reduces the problem dimension by one. Sorting + duplicate skipping ensures uniqueness.

## Key Insight
4Sum = fix two elements + Two Sum II on the rest. Each fixed element reduces the problem by one dimension. The pattern generalizes: kSum = fix one + (k-1)Sum.

## Edge Cases
- All elements identical → at most one quadruplet
- Target is very large or very negative (use long arithmetic if needed)
- Duplicate values in input → must skip at each pointer level
- Array length < 4 → empty list
