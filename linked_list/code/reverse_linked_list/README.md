# Reverse Linked List (LC 206)

Reverse a singly linked list and return the new head.

## Approaches

### 1. Iterative
- **Time:** O(n) | **Space:** O(1)
- Track `prev = None` and `curr = head`. For each node: save `curr.next`, point `curr.next` to `prev`, advance both pointers.
- Return `prev` (the new head) when `curr` is None.

### 2. Recursive
- **Time:** O(n) | **Space:** O(n) call stack
- Recurse to the end of the list. On the way back, make `head.next.next = head` and `head.next = None`.
- The last node becomes the new head and is returned up the call stack.

## Key Insight

Iterative: we're re-wiring each node's `next` pointer to point backward. The `prev` pointer tracks the already-reversed portion. Three-pointer dance: save next, reverse link, advance.

Recursive: the base case is the last node (new head). On the way back up, each node's successor is made to point back at it, and the forward link is severed. Elegant but uses O(n) stack space.

## Edge Cases

- Empty list (`head = None`) → return None.
- Single node → return that node unchanged.
- Two nodes: `[1, 2]` → `[2, 1]`.
