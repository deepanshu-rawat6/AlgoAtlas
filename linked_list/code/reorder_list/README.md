# Reorder List (LC 143)

Reorder `L0 → L1 → … → Ln` to `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …` in-place.

## Approaches

### 1. Array of Nodes
- **Time:** O(n) | **Space:** O(n)
- Collect all nodes into an array. Use two pointers (`lo`, `hi`) to interleave from both ends.

### 2. Find Middle + Reverse + Merge (Optimal)
- **Time:** O(n) | **Space:** O(1)
- **Step 1:** Find the middle using slow/fast pointers. Split the list into two halves.
- **Step 2:** Reverse the second half in-place.
- **Step 3:** Merge the two halves alternately: take one from first, one from second.

## Key Insight

The reordering pattern is exactly "first half interleaved with reversed second half." Reversing the second half transforms the problem into a simple merge of two lists. The slow/fast pointer finds the midpoint in one pass. Splitting at `slow.next = None` prevents the merge from running into the original second half.

## Edge Cases

- Single node: no reordering needed, return immediately.
- Two nodes: `[1, 2]` → `[1, 2]` (already in order).
- Even vs odd length: slow/fast pointer correctly finds the end of the first half in both cases.
- The merge loop terminates when `second` is None (second half may be shorter by 1 for odd-length lists).
