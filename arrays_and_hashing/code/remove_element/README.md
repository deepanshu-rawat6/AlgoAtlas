# Remove Element (LC 27)

Given an integer array `nums` and integer `val`, remove all occurrences of `val` in-place.
Return `k` — the count of elements not equal to `val`. The first `k` elements of `nums` must hold the result.

## Approaches

### 1. Shift Left — O(n²) time, O(1) space
When `val` is found, shift all subsequent elements left by one. Repeat.

**Why it works:** Correct but O(n²) due to repeated shifting — each removal costs O(n).

### 2. Two Pointers (Write Pointer) — O(n) time, O(1) space
Use `k` as a write pointer. Scan with `i`; whenever `nums[i] != val`, copy it to `nums[k]` and advance `k`.

**Why it works:** The write pointer only advances when a valid element is found, compacting all non-`val` elements to the front in a single pass.

## Key Insight
Write pointer pattern: one pointer reads, one pointer writes. The write pointer only advances on valid elements, naturally skipping all occurrences of `val`.

## Edge Cases
- `val` not present in array → `k == len(nums)`, array unchanged
- All elements equal `val` → `k == 0`
- Empty array → `k == 0`
- `val` appears only at the end
