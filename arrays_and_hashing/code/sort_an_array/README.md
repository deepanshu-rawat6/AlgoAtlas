# Sort an Array (LC 912)

Given an array of integers `nums`, sort it in ascending order in O(n log n) time
without using built-in sort functions.

## Approaches

### 1. Merge Sort — O(n log n) time, O(n) space
Recursively split the array in half, sort each half, then merge the two sorted halves.

**Why it works:** Divide and conquer — merging two sorted arrays is O(n), and the recursion depth is O(log n), giving O(n log n) total.

### 2. Quick Sort (Randomized) — O(n log n) average, O(log n) space
Pick a random pivot, partition elements around it, recursively sort both sides.

**Why it works:** Randomized pivot avoids worst-case O(n²) on sorted input. On average, each partition splits the array roughly in half.

### 3. Heap Sort — O(n log n) time, O(1) space
Build a max-heap in-place, then repeatedly extract the max to the end of the array.

**Why it works:** A max-heap always gives the largest element in O(1). Extracting n times with O(log n) heapify each time gives O(n log n) with no extra space.

## Key Insight
Heap sort is the only O(n log n) + O(1) space comparison sort. Use it when memory is constrained; merge sort when stability matters.

## Edge Cases
- Already sorted array → quick sort degrades without randomization
- All elements identical → all approaches handle correctly
- Negative numbers
- Single element or empty array
