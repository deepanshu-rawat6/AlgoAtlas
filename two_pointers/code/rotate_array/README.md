# Rotate Array (LC 189)

Given an integer array `nums`, rotate it to the right by `k` steps in-place.

## Approaches

### 1. Brute Force — O(n·k) time, O(1) space
Rotate one step at a time: save the last element, shift everything right, place saved element at front.

**Why it works:** Correct but O(n·k) — impractical when k is large.

### 2. Extra Array — O(n) time, O(n) space
Slice: `nums[-k:] + nums[:-k]` gives the rotated array. Copy back into `nums`.

**Why it works:** Slicing directly computes the rotated layout. Uses O(n) extra space.

### 3. Three Reversals — O(n) time, O(1) space
Reverse the entire array, then reverse the first `k` elements, then reverse the remaining `n-k` elements.

**Why it works:** Reversing the whole array puts the last `k` elements at the front (in reverse order). Reversing each segment separately corrects their internal order. Three reversals = one rotation.

## Key Insight
Three reversals achieve rotation in O(1) space. Remember to normalize `k = k % n` first to handle `k > n`.

## Edge Cases
- `k == 0` or `k == n` → no change (handle with `k %= n`)
- `k > n` → equivalent to `k % n` steps
- Single element → no change
- All elements identical → no visible change
