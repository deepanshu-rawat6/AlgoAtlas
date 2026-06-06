# Remove Duplicates from Sorted Array (LC 26)

Given a sorted array `nums`, remove duplicates in-place so each unique element appears once.
Return `k` — the count of unique elements. The first `k` elements must hold the result.

## Approaches

### 1. Set + Overwrite — O(n) time, O(n) space
Collect unique elements via a set, sort them, overwrite `nums`.

**Why it works:** Correct but uses O(n) extra space and ignores the sorted property.

### 2. Two Pointers — O(n) time, O(1) space
`k` is the write pointer starting at 1. Scan with `i`; when `nums[i] != nums[i-1]`, a new unique element is found — write it to `nums[k]` and advance `k`.

**Why it works:** The array is sorted, so duplicates are always adjacent. A new unique element is detected by comparing to the previous element. The write pointer compacts unique elements to the front.

## Key Insight
Sorted array means duplicates are adjacent. Compare each element to its predecessor — a difference signals a new unique value to keep.

## Edge Cases
- Single element → `k == 1`, no changes
- All elements identical → `k == 1`
- All elements distinct → `k == len(nums)`, no changes
- Two elements, both same → `k == 1`
