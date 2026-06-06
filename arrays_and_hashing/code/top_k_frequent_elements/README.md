# Top K Frequent Elements (LC 347)

Given an integer array `nums` and integer `k`, return the `k` most frequent elements.
The answer is guaranteed to be unique; order doesn't matter.

## Approaches

### 1. Sort by Frequency — O(n log n) time, O(n) space
Count frequencies with a hash map, then sort by descending frequency and take the first `k`.

**Why it works:** Sorting by frequency directly ranks elements by how often they appear.

### 2. Min-Heap of Size k — O(n log k) time, O(n) space
Use `heapq.nlargest(k, ...)` which maintains a min-heap of size `k` while scanning.

**Why it works:** A heap of size `k` keeps only the top-k candidates, reducing the log factor from n to k.

### 3. Bucket Sort — O(n) time, O(n) space
Create `n+1` buckets indexed by frequency. Fill buckets, then iterate from highest frequency down until `k` elements are collected.

**Why it works:** Frequency is bounded by `n`, so we can use frequency as a direct array index — no comparison-based sorting needed.

## Key Insight
Bucket sort achieves O(n) by exploiting the fact that frequency is bounded by array length, turning sorting into direct indexing.

## Edge Cases
- `k == 1` → return the single most frequent element
- All elements have the same frequency → any `k` of them are valid
- `k == len(unique elements)` → return all unique elements
