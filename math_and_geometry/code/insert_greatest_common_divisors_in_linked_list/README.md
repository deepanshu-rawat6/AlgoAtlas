# LC 2807 — Insert Greatest Common Divisors in Linked List

Given the head of a linked list, insert a new node with value `gcd(a, b)` between every pair of adjacent nodes `a` and `b`. Return the modified list.

## Approaches

### 1. Single Pass Insertion
- **Time:** O(n) | **Space:** O(1)
- Traverse the list. For each node `cur` with a next node, compute `gcd(cur.val, cur.next.val)`, create a new node with that value, and splice it between `cur` and `cur.next`. Advance `cur` by two steps (skip the newly inserted node).

## Key Insight

The key is advancing `cur = cur.next.next` after each insertion — skipping the newly inserted GCD node to avoid processing it as a pair. The insertion is a standard linked list splice: `cur.next = ListNode(g, cur.next)`. Since we process pairs left to right and each pair is independent, a single pass suffices.

## Edge Cases

- Single node: No pairs to process, return the node unchanged.
- Two nodes: Insert one GCD node between them.
- All nodes with the same value `v`: All inserted nodes have value `v` (gcd(v, v) = v).
- Adjacent nodes where one divides the other: GCD equals the smaller value.
