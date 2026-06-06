# Majority Element II (LC 229)

Given an integer array of size `n`, find all elements that appear more than ⌊n/3⌋ times.
There can be at most two such elements.

## Approaches

### 1. Hash Map — O(n) time, O(n) space
Count all element frequencies. Return those exceeding `n // 3`.

**Why it works:** Direct frequency counting identifies all qualifying elements in one pass.

### 2. Boyer-Moore Extended — O(n) time, O(1) space
Maintain two candidates with vote counts. When a new element matches neither candidate and a count is zero, replace that candidate. Otherwise decrement both counts. Verify the two final candidates with a count pass.

**Why it works:** At most 2 elements can exceed n/3. The voting algorithm cancels out groups of 3 distinct elements, leaving only the true majority candidates. A verification pass confirms they actually meet the threshold.

## Key Insight
At most 2 elements can appear more than n/3 times (since 3 × (n/3+1) > n). Boyer-Moore extended tracks exactly 2 candidates using the same cancellation logic as the classic majority vote.

## Edge Cases
- Single element → always qualifies
- Two elements with equal frequency → both may qualify
- No element exceeds n/3 → return empty list
- All elements identical → one result
- Array of length 1 or 2 → all elements qualify
