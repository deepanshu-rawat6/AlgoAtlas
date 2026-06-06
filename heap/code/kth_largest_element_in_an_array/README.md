# Kth Largest Element in an Array (LC 215)

Return the k-th largest element in an unsorted array (not k-th distinct).

## Approaches

### Sort
- **Time:** O(n log n)
- **Space:** O(1)
- Sort descending, return index k-1. Straightforward but over-sorts.

### Min-Heap of Size k
- **Time:** O(n log k)
- **Space:** O(k)
- Maintain a min-heap of size k. After processing all elements, the heap top is the k-th largest (smallest of the top-k).

### Quickselect (optimal average)
- **Time:** O(n) average, O(n²) worst
- **Space:** O(1)
- The k-th largest is at index `n - k` in sorted-ascending order. Partition around a pivot; if pivot lands at `n-k`, done. Otherwise recurse on the relevant half.

## Key Insight

Quickselect avoids sorting the entire array. The partition invariant guarantees that after each step, elements before the pivot are ≤ pivot and elements after are ≥ pivot. Once the pivot index equals the target, the value at that index is the answer — no further work needed.

## Edge Cases

- k = 1 → return the maximum.
- k = n → return the minimum.
- Duplicate values: the k-th largest counts by position, not by distinct value (e.g., `[3,3,3]`, k=2 → 3).
- Worst-case quickselect (already sorted + bad pivot choice) degrades to O(n²); randomizing the pivot mitigates this.
