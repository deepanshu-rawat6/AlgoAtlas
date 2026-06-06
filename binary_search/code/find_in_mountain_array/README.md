# Find in Mountain Array (LC 1095)

Given a mountain array (accessible only via API), find the minimum index where `mountainArr.get(index) == target`. Limited to 100 API calls.

## Approaches

### 1. Three-Phase Binary Search
- **Time:** O(log n) | **Space:** O(1)
- **Phase 1 — Find Peak:** Binary search where `arr[mid] < arr[mid+1]` means peak is to the right.
- **Phase 2 — Search Ascending Left Half `[0, peak]`:** Standard binary search (ascending order).
- **Phase 3 — Search Descending Right Half `[peak+1, n-1]`:** Binary search with reversed comparisons (descending order).
- Return the left-half result if found (smaller index); otherwise return right-half result.

## Key Insight

A mountain array has two monotone halves. We must find the peak first to know the boundaries of each half. Searching the left half first ensures we return the **minimum index** (left half indices are always smaller). The descending right half requires flipping the binary search direction: `val > target` means go right (values decrease going right).

The 100-call limit is satisfied: each phase uses O(log n) calls, and n ≤ 10⁴ → log₂(10⁴) ≈ 14 calls per phase → ~42 total.

## Edge Cases

- Target at the peak: found in Phase 2 (left half includes peak).
- Target only in right half: Phase 2 returns -1, Phase 3 finds it.
- Target not in array: both phases return -1.
- Target equals first or last element: boundary conditions handled by standard binary search.
- Multiple occurrences: left half is checked first, guaranteeing minimum index.
