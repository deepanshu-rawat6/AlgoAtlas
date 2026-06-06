# Sorting Algorithms

## Comparison Table

| Algorithm      | Best       | Average    | Worst      | Space    | Stable | In-Place |
|----------------|------------|------------|------------|----------|--------|----------|
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅     | ❌       |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | ❌     | ✅       |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | ❌     | ✅       |
| Counting Sort  | O(n+k)     | O(n+k)     | O(n+k)     | O(k)     | ✅     | ❌       |
| Bucket Sort    | O(n+k)     | O(n+k)     | O(n²)      | O(n+k)   | ✅*    | ❌       |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅     | ✅       |
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅     | ✅       |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | ❌     | ✅       |

*Bucket sort stability depends on the inner sort used.

## When to Use What

- **Merge Sort** — need guaranteed O(n log n), need stability, sorting linked lists
- **Quick Sort** — general purpose, cache-friendly, average-case performance matters
- **Heap Sort** — need O(1) space + O(n log n) worst case (e.g., real-time systems)
- **Counting Sort** — integers in a small known range (e.g., ages, scores 0–100)
- **Bucket Sort** — uniformly distributed floats in [0, 1), or when data fits in buckets

## Files

- `merge_sort.py` — top-down and bottom-up merge sort
- `quick_sort.py` — Lomuto and Hoare partition schemes, randomized pivot
- `heap_sort.py` — sift_down, build_heap, heap sort
- `counting_sort.py` — stable counting sort for integers
- `bucket_sort.py` — bucket sort for floats
