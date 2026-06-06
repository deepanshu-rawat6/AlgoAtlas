# Implement Queue using Stacks (LC 232)

Implement a FIFO queue using only two stacks, supporting `push`, `pop`, `peek`, and `empty`.

## Approaches

### 1. Two Stacks — Costly Push
- **Time:** O(n) push, O(1) pop/peek | **Space:** O(n)
- On `push(x)`: drain s1 into s2, push x to s1 (now at bottom), drain s2 back into s1.
- The oldest element is always at the top of s1, so `pop` and `peek` are O(1).

### 2. Two Stacks — Amortized O(1) (Lazy Transfer)
- **Time:** O(1) amortized all ops | **Space:** O(n)
- `push` always goes to `inbox`. `pop`/`peek` use `outbox`.
- Transfer inbox → outbox only when outbox is empty. Each element is moved at most once.
- This is the optimal approach: O(1) amortized for all operations.

## Key Insight

A stack reverses order; two reversals restore FIFO order. The lazy approach defers the reversal until necessary — if outbox still has elements, they're already in the right order. Each element crosses from inbox to outbox exactly once, giving O(1) amortized cost.

## Edge Cases

- Interleaved pushes and pops: outbox may still have elements when new items are pushed to inbox — don't transfer until outbox is empty.
- `empty()` must check both stacks (inbox and outbox).
- All calls to `pop` and `peek` are guaranteed valid.
