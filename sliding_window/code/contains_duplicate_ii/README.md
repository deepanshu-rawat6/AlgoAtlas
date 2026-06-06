# Contains Duplicate II (LC 219)

Given an integer array `nums` and integer `k`, return `true` if there exist two distinct
indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Approaches

### 1. Brute Force — O(n·k) time, O(1) space
For each element, check the next `k` elements for a duplicate.

**Why it works:** Correct but slow — checks up to k elements per position.

### 2. Sliding Window Set — O(n) time, O(k) space
Maintain a set of the last `k` elements (a sliding window). For each new element, check if it's already in the set. If yes, return `true`. Add it to the set and remove the element that just fell out of the window.

**Why it works:** The set always contains exactly the elements within distance `k` of the current position. A hit means a duplicate within the required distance.

## Key Insight
A set of size `k` acts as a sliding window. Membership check is O(1), and the window is maintained by removing `nums[i - k]` when the window exceeds size `k`.

## Edge Cases
- `k == 0` → no two distinct indices can have distance 0, return `false`
- All elements identical → `true` if `k >= 1`
- No duplicates at all → `false`
- `k >= len(nums)` → reduces to Contains Duplicate (LC 217)
