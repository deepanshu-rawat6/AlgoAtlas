# LC 99 — Recover Binary Search Tree

## Problem Statement
Two nodes of a BST are swapped by mistake. Recover the tree without changing its
structure (fix the values in-place).

**Example:**
- Input: [1,3,null,null,2] (3 and 1 are swapped)
- Output: [3,1,null,null,2]

**Constraints:** Number of nodes in [2, 1000], -2^31 ≤ val ≤ 2^31 - 1.

---

## Approaches

### Approach 1 — Inorder to Array (O(n) time, O(n) space)
1. Collect all nodes via inorder traversal.
2. Scan for violations: a violation is where `nodes[i].val > nodes[i+1].val`.
   - First violation: `first = nodes[i]`, `second = nodes[i+1]`.
   - Second violation (if any): update `second = nodes[i+1]`.
3. Swap `first.val` and `second.val`.

Two violations → non-adjacent swap. One violation → adjacent swap.

### Approach 2 — Morris Traversal (O(n) time, O(1) space)
Morris traversal achieves inorder traversal without a stack or recursion by
temporarily threading right pointers to inorder successors:
- When visiting a node, compare with `prev` to detect violations.
- Track `first` and `second` exactly as in Approach 1.
- After traversal, swap the two nodes' values.

Optimal space complexity — no extra data structures.

---

## Key Insight
The inorder traversal of a valid BST is strictly sorted. Swapping two nodes creates
exactly one or two "descents" (places where a value is greater than the next).
- Two descents: `first` = larger element at descent 1, `second` = smaller at descent 2.
- One descent (adjacent swap): `first` and `second` are the two elements in that descent.

---

## Complexity
| Approach         | Time | Space |
|------------------|------|-------|
| Inorder array    | O(n) | O(n)  |
| Morris traversal | O(n) | O(1)  |

---

## Edge Cases
- Adjacent swap → only one descent in inorder; `second` is set only once.
- Non-adjacent swap → two descents; `second` is updated at the second descent.
- Minimum tree (2 nodes) → one of the two nodes is always swapped with the other.
- Root is one of the swapped nodes → handled correctly by both approaches.
