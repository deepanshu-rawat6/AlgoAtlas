# 3Sum (LC 15)

Given an integer array `nums`, return all unique triplets `[a, b, c]` such that
`a + b + c == 0`. The solution set must not contain duplicate triplets.

## Approaches

### 1. Brute Force — O(n³) time, O(n) space
Try all triplets; use a set to deduplicate.

**Why it works:** Exhaustive search finds all valid triplets, but is too slow for large inputs.

### 2. Sort + Two Pointers — O(n²) time, O(1) extra space
Sort the array. Fix one element `i`, then use two pointers `lo` and `hi` for the remaining pair. Skip duplicate values at each level to avoid duplicate triplets.

**Why it works:** Sorting enables two-pointer convergence for the inner pair (same as Two Sum II). Skipping duplicates at each pointer position ensures uniqueness without a set.

## Key Insight
Fix one element, reduce to Two Sum II on the rest. Sorting + duplicate skipping handles uniqueness in O(1) extra space.

## Edge Cases
- All zeros `[0,0,0]` → one triplet `[0,0,0]`
- No valid triplet → empty list
- Duplicate values in input → must skip to avoid duplicate triplets
- Array length < 3 → empty list
