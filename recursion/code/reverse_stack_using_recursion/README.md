# Reverse Stack Using Recursion

Reverse a stack using only recursion — no auxiliary data structures allowed.

## Approaches

### 1. Pop + Reverse + Insert at Bottom
- **Time:** O(n²) | **Space:** O(n) call stack
- `reverseStack`: pop the top, recursively reverse the remaining stack, then insert the popped element at the bottom using `_insertAtBottom`.
- `_insertAtBottom`: if stack is empty, push the value. Otherwise, pop the top, recurse to insert at bottom, then restore the top.

## Key Insight

Reversing a stack requires two recursive functions working together. `reverseStack` peels off the top and reverses the rest, but then needs to place the top at the bottom — which itself requires recursion (`_insertAtBottom`). The call stack acts as the only auxiliary storage. The O(n²) complexity comes from `_insertAtBottom` being called n times, each taking O(n) stack frames.

## Edge Cases

- Empty stack: Return as-is.
- Single element: Already reversed.
- `[1, 2, 3]` (top=3): Becomes `[3, 2, 1]` (top=1).
- The list is treated as a stack with the last element as the top.
