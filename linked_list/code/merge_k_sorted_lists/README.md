# Merge K Sorted Lists (LC 23)

Merge k sorted linked lists into one sorted linked list.

## Approaches

### 1. Sequential Merge
- **Time:** O(kN) | **Space:** O(1)
- Merge lists one by one using the two-list merge. Each merge is O(current_size + next_list_size), leading to O(kN) total.

### 2. Divide and Conquer
- **Time:** O(N log k) | **Space:** O(log k) call stack
- Pair up lists and merge pairs. Repeat until one list remains.
- Each round halves the number of lists; there are log k rounds, each touching all N nodes.

### 3. Min Heap
- **Time:** O(N log k) | **Space:** O(k)
- Push the head of each list into a min-heap. Repeatedly pop the minimum node, append to result, and push that node's `next` (if any).
- The heap always has at most k elements.

## Key Insight

Sequential merge is simple but inefficient — early lists get merged repeatedly. Divide and conquer and the heap both achieve O(N log k) by ensuring each node is processed O(log k) times (D&C) or each heap operation costs O(log k) (heap).

The heap approach is the most practical: it processes nodes in globally sorted order without restructuring the list array.

## Edge Cases

- Empty `lists` array → return None.
- Lists containing only None entries → handled by skipping None heads.
- Single list → return it directly.
- Lists of very different lengths → all approaches handle this correctly.
