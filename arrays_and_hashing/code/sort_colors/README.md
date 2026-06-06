# Sort Colors (LC 75)

Given an array `nums` with values 0 (red), 1 (white), 2 (blue), sort it in-place
so colors are in order 0, 1, 2. No library sort allowed.

## Approaches

### 1. Counting Sort — O(n) time, O(1) space, two passes
Count occurrences of 0, 1, 2. Overwrite the array with the correct counts in order.

**Why it works:** Only three distinct values, so counting is trivial. Two passes: one to count, one to fill.

### 2. Dutch National Flag — O(n) time, O(1) space, one pass
Three pointers: `lo` (boundary of 0s), `mid` (current), `hi` (boundary of 2s).
- `nums[mid] == 0`: swap with `lo`, advance both
- `nums[mid] == 1`: advance `mid`
- `nums[mid] == 2`: swap with `hi`, shrink `hi` (don't advance `mid` — unknown value came from `hi`)

**Why it works:** Maintains three invariant regions simultaneously. Each element is placed in its correct region in at most one swap.

## Key Insight
Dutch National Flag: after a swap with `hi`, don't advance `mid` — the swapped-in value is unknown and must be re-examined.

## Edge Cases
- All same color → no swaps needed
- Already sorted → no swaps needed
- Single element
- Only two distinct colors present
