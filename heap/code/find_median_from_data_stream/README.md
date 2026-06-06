# Find Median from Data Stream (LC 295)

Design a data structure that supports adding integers from a stream and returning the current median at any time.

## Approaches

### Sorted Insert (bisect)
- **Time:** O(n) per `addNum` (insertion shift), O(1) `findMedian`
- **Space:** O(n)
- Maintain a sorted list using `bisect.insort`. Median is the middle element (or average of two middle elements). Simple but O(n) insertion.

### Two Heaps (optimal)
- **Time:** O(log n) per `addNum`, O(1) `findMedian`
- **Space:** O(n)
- Maintain two heaps: `small` (max-heap via negation) for the lower half, `large` (min-heap) for the upper half. Invariants: every element in `small` ≤ every element in `large`; sizes differ by at most 1 (`small` can have one extra).
- `addNum`: push to `small`; if `small`'s max > `large`'s min, rebalance; then balance sizes.
- `findMedian`: if sizes equal, average the two tops; otherwise return `small`'s top.

## Key Insight

The two-heap structure splits the stream at the median. `small` holds the bottom half and `large` holds the top half. The median is always at the boundary — either the top of `small` (odd total) or the average of both tops (even total). Rebalancing after each insert maintains the invariant in O(log n).

## Edge Cases

- Single element → median is that element.
- Two elements → median is their average.
- Negative numbers → negation trick still works correctly.
- Large stream with many duplicates → heaps handle duplicates naturally.
