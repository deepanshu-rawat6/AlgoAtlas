# Implement Stack using Queues (LC 225)

Implement a LIFO stack using only two queues, supporting `push`, `pop`, `top`, and `empty`.

## Approaches

### 1. Two Queues — Costly Push
- **Time:** O(n) push, O(1) pop/top | **Space:** O(n)
- On `push(x)`: enqueue x into q2, then drain all of q1 into q2, then swap q1 and q2.
- This ensures the most recently pushed element is always at the front of q1.
- `pop` and `top` are O(1) since the stack top is always at q1's front.

### 2. Two Queues — Costly Pop
- **Time:** O(1) push, O(n) pop/top | **Space:** O(n)
- On `push(x)`: simply enqueue to q1.
- On `pop`: drain all but the last element into q2, return the last, then swap.
- Trade-off: push is cheap but pop/top are expensive.

## Key Insight

A queue is FIFO; a stack is LIFO. The trick is to **reverse the order** of elements so the newest is always accessible at the front. Costly-push does this eagerly on every insert; costly-pop does it lazily only when needed. Both approaches pay O(n) somewhere — the choice depends on whether reads or writes are more frequent.

## Edge Cases

- Single element: push then pop should return that element and leave the stack empty.
- All calls to `pop` and `top` are guaranteed valid (non-empty stack).
- Maximum 100 calls — both approaches are fine within constraints.
