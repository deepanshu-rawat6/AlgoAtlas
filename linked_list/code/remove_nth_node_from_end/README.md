# Remove Nth Node From End of List (LC 19)

Remove the nth node from the end of a linked list in one pass.

## Approaches

### 1. Two Pass
- **Time:** O(n) | **Space:** O(1)
- First pass: count the length. Second pass: advance to position `length - n`, then skip the next node.

### 2. Two Pointers (One Pass)
- **Time:** O(n) | **Space:** O(1)
- Use a dummy head. Advance `fast` pointer `n + 1` steps ahead of `slow`.
- Move both until `fast` is None. Now `slow` is just before the node to remove.
- `slow.next = slow.next.next`.

## Key Insight

The gap of `n + 1` between `fast` and `slow` ensures that when `fast` falls off the end (becomes None), `slow` is exactly at the node **before** the one to delete. The `+1` is crucial — it positions `slow` at the predecessor, not the target itself, so we can do the deletion.

The dummy head handles the edge case of removing the first node (when `n == length`).

## Edge Cases

- Remove the only node (`n = 1`, single-element list) → dummy head ensures `slow` is the dummy, `slow.next = slow.next.next` works.
- Remove the first node (`n == length`) → `fast` advances past the end, `slow` stays at dummy.
- Remove the last node (`n = 1`) → `slow` ends up at the second-to-last node.
