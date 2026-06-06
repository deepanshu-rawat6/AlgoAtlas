# Linked List Cycle (LC 141)

Determine if a linked list has a cycle.

## Approaches

### 1. Hash Set
- **Time:** O(n) | **Space:** O(n)
- Track visited node identities. If a node is seen twice, there's a cycle.

### 2. Floyd's Cycle Detection (Two Pointers)
- **Time:** O(n) | **Space:** O(1)
- `slow` moves 1 step, `fast` moves 2 steps. If they ever point to the same node, there's a cycle.
- If `fast` or `fast.next` becomes None, the list is finite (no cycle).

## Key Insight

If there's a cycle, `fast` laps `slow` inside the cycle — they must meet. The relative speed difference is 1 step per iteration, so `fast` gains on `slow` by 1 node each step and will eventually catch up. If there's no cycle, `fast` reaches the end in O(n/2) steps.

The hash set approach is simpler but uses O(n) space. Floyd's algorithm is the classic O(1) space solution.

## Edge Cases

- Empty list (`head = None`) → no cycle, return False.
- Single node with no self-loop → `fast.next` is None → False.
- Single node with self-loop (`node.next = node`) → `slow == fast` on first iteration → True.
- Cycle at the very beginning (tail connects to head).
