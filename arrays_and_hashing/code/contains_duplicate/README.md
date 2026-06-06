# Contains Duplicate (LC 217)

Given an integer array `nums`, return `true` if any value appears at least twice,
and `false` if every element is distinct.

## Approaches

### 1. Brute Force — O(n²) time, O(1) space
Compare every pair `(i, j)`. Return `true` on first match.

**Why it works:** Exhaustive comparison catches any duplicate, but is slow for large inputs.

### 2. Sort — O(n log n) time, O(1) space
Sort the array; duplicates become adjacent. One linear scan detects them.

**Why it works:** Sorting groups equal elements together, so a duplicate always appears next to itself.

### 3. Hash Set — O(n) time, O(n) space
Convert to a set. If `len(set(nums)) != len(nums)`, a duplicate existed.

**Why it works:** A set collapses duplicates — any size reduction means at least one value appeared more than once.

## Key Insight
A set's deduplication property makes duplicate detection a one-liner: compare original length to set length.

## Edge Cases
- Single-element array → always `false`
- All elements identical → `true`
- Negative numbers (handled naturally by hash set)
