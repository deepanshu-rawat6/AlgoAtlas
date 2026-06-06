# Reverse Nodes in k-Group (LC 25)

Reverse every k consecutive nodes in a linked list. If fewer than k nodes remain at the end, leave them as-is.

## Approaches

### 1. Iterative
- **Time:** O(n) | **Space:** O(1)
- Use a dummy head and `group_prev` pointer. For each group:
  1. Check if k nodes remain (advance `kth` pointer k times).
  2. Reverse the k nodes in-place.
  3. Reconnect: `group_prev.next = kth` (new group head), advance `group_prev` to the old group head (now tail).

### 2. Recursive
- **Time:** O(n) | **Space:** O(n/k) call stack
- Count k nodes; if fewer remain, return head unchanged.
- Reverse k nodes, then set `head.next = reverseKGroup(remaining, k)`.
- Return the new head of the reversed group.

## Key Insight

After reversing a group, the original first node becomes the tail. The tail must connect to the result of processing the rest of the list. In the recursive approach, `head` (original first node) becomes the tail, so `head.next = recurse(...)` naturally wires it up. In the iterative approach, `group_prev` is updated to the old group head (new tail) before moving to the next group.

## Edge Cases

- `k = 1`: no reversal, return list unchanged.
- `k = n`: reverse the entire list.
- Remaining nodes < k: left as-is (the check for k nodes before reversing handles this).
- Single node with `k = 1`: return as-is.
