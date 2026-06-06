# Search in Rotated Sorted Array II (LC 81)

Same as LC 33 but the array may contain **duplicates**. Return true/false instead of an index.

## Approaches

### 1. Linear Scan
- **Time:** O(n) | **Space:** O(1)
- `return target in nums`.

### 2. Binary Search with Duplicate Handling
- **Time:** O(log n) average, O(n) worst | **Space:** O(1)
- Same half-identification as LC 33, but add one case: when `nums[lo] == nums[mid] == nums[hi]`, we can't determine which half is sorted → shrink both ends by 1 (`lo += 1`, `hi -= 1`).
- Otherwise, proceed with the same sorted-half logic as LC 33.

## Key Insight

Duplicates break the half-identification: if `nums[lo] == nums[mid]`, the left half might be `[1,1,1,3,1]` (not sorted) or `[1,1,1,1,1]` (sorted). We can't tell. The fix is to shrink bounds when all three (lo, mid, hi) are equal — this is the only ambiguous case. This degrades to O(n) in the worst case (all duplicates), but is O(log n) on average.

## Edge Cases

- All same elements, target present → O(n) worst case (shrink by 1 each iteration).
- All same elements, target absent → O(n) worst case.
- `[1,1,1,1,1,1,13,1,1,1,1]` with target 13 → duplicates force linear-like scan until 13 is found.
- No duplicates → identical to LC 33 behavior.
