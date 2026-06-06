# Kth Largest Element in a Stream (LC 703)

Design a class that finds the k-th largest element in a stream. `add(val)` appends a value and returns the current k-th largest.

## Approaches

### Sort on Every Add
- **Time:** O(n log n) per `add` — insert via `bisect.insort` then index from end
- **Space:** O(n)
- Keep a sorted list; `add` inserts in sorted position; return `list[-k]`. Simple but slow for large streams.

### Min-Heap of Size k (optimal)
- **Time:** O(n log k) init, O(log k) per `add`
- **Space:** O(k)
- Maintain a min-heap of exactly k elements. The heap top is always the k-th largest. On `add`: push the new value; if heap size exceeds k, pop the minimum (it's outside the top-k). The top of the heap is the answer.

## Key Insight

A min-heap of size k is a "window" that keeps only the k largest elements seen so far. The smallest element in this window is the k-th largest overall. Evicting the minimum when the heap grows beyond k ensures the invariant holds after every insertion.

## Edge Cases

- Initial `nums` can be empty — heap starts empty and fills as `add` is called.
- Values smaller than all current top-k elements are pushed then immediately popped.
- k = 1 → heap always holds just the maximum; `add` returns the running maximum.
- Duplicate values are handled correctly since the heap doesn't require uniqueness.
