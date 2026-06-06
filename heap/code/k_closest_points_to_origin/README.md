# K Closest Points to Origin (LC 973)

Return the k points closest to the origin (0, 0) using Euclidean distance. Order doesn't matter.

## Approaches

### Sort
- **Time:** O(n log n)
- **Space:** O(1) extra (in-place sort)
- Sort all points by squared distance (`x²+y²`), return first k. Simple and correct; no need for `sqrt` since it's monotone.

### Max-Heap of Size k
- **Time:** O(n log k)
- **Space:** O(k)
- Maintain a max-heap of size k using negated distances. For each point, push it; if heap exceeds k, pop the farthest. Remaining heap contains the k closest.

### Quickselect (optimal average)
- **Time:** O(n) average, O(n²) worst
- **Space:** O(1) extra
- Partition the array around a pivot distance. If the pivot lands at index k-1, the first k elements are the answer. Otherwise recurse on the relevant half. No need to fully sort.

## Key Insight

Quickselect finds the k-th order statistic without sorting the entire array. The partition step places elements ≤ pivot before it and > pivot after it — once the pivot is at index k-1, everything to its left is in the answer set (though not sorted among themselves).

## Edge Cases

- k equals the total number of points → return all points.
- Multiple points at the same distance → any valid selection is accepted.
- Points with negative coordinates — squared distance handles this correctly.
