# Merge Sorted Array (LC 88)

Merge sorted array `nums2` (length `n`) into sorted array `nums1` (length `m+n`, last `n` slots are 0).
Modify `nums1` in-place.

## Approaches

### 1. Copy + Sort — O((m+n) log(m+n)) time, O(n) space
Copy `nums2` into the spare slots of `nums1`, then sort.

**Why it works:** Correct but ignores the fact that both arrays are already sorted.

### 2. Fill from the End — O(m+n) time, O(1) space
Use three pointers: `i` at end of `nums1`'s valid elements, `j` at end of `nums2`, `k` at end of `nums1`. Compare `nums1[i]` and `nums2[j]`, place the larger at `nums1[k]`, move that pointer left.

**Why it works:** Filling from the back avoids overwriting unprocessed elements in `nums1`. The spare zeros at the end provide safe write space.

## Key Insight
Fill from the end: writing backwards into `nums1`'s spare space means we never overwrite elements we haven't processed yet.

## Edge Cases
- `m == 0` → just copy `nums2` into `nums1`
- `n == 0` → `nums1` is already correct
- All elements of `nums2` are larger than all of `nums1`
- All elements of `nums2` are smaller than all of `nums1`
