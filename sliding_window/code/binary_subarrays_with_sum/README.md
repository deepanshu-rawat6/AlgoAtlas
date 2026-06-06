# Binary Subarrays With Sum (LC 930)

Given a binary array `nums` and integer `goal`, return the number of non-empty subarrays
with sum equal to `goal`.

## Approaches

### 1. Prefix Sum + Hash Map — O(n) time, O(n) space
Track running prefix sum. For each position, count how many previous prefix sums equal `prefix - goal`. Those positions form subarrays ending here with sum exactly `goal`.

**Why it works:** `prefix[j] - prefix[i] == goal` means the subarray `nums[i+1..j]` sums to `goal`. Counting stored prefix sums equal to `prefix - goal` counts all such subarrays ending at `j`.

### 2. atMost(goal) - atMost(goal-1) — O(n) time, O(1) space
`exactly(k) = atMost(k) - atMost(k-1)`. Each `atMost` is a standard sliding window.

**Why it works:** Exact-count problems on binary arrays can be decomposed into two at-most problems. The sliding window for at-most is straightforward; the difference gives the exact count.

## Key Insight
`exactly(k) = atMost(k) - atMost(k-1)` — a powerful trick that converts exact-count sliding window problems into two simpler at-most problems.

## Edge Cases
- `goal == 0` → count subarrays of all zeros (many when zeros are consecutive)
- All ones, `goal == len(nums)` → one subarray
- No subarray reaches `goal` → 0
- Binary array with no zeros → only contiguous 1-subarrays count
