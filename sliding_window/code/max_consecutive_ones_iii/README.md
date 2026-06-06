# Max Consecutive Ones III (LC 1004)

Given a binary array `nums` and integer `k`, return the maximum number of consecutive 1s
if you can flip at most `k` zeros.

## Approaches

### 1. Sliding Window — O(n) time, O(1) space
Expand right always. Track the count of zeros in the window. When zeros exceed `k`, shrink from the left (decrement zero count if the removed element was 0). Track the maximum window size.

**Why it works:** The window represents a valid segment where at most `k` zeros exist (i.e., can be flipped to 1). Shrinking restores validity when too many zeros accumulate.

## Key Insight
"Flip at most k zeros" = "window with at most k zeros." Standard sliding window: expand right, shrink left when zero count exceeds k.

## Edge Cases
- `k == 0` → longest run of existing 1s
- All zeros, `k >= len(nums)` → entire array
- All ones → entire array regardless of `k`
- `k > count of zeros` → entire array
