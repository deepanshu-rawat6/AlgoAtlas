# LC 285 / 510 — Inorder Successor and Predecessor in BST

## Problem Statement
Given a BST and a node `p`:
- **Inorder Successor**: the node with the smallest value **greater than** `p.val`.
- **Inorder Predecessor**: the node with the largest value **less than** `p.val`.

Return `None` if no such node exists.

**Example:**
- BST = [5,3,6,2,4,null,null,1], p = 3
- Successor = 4, Predecessor = 2

---

## Approaches

### Approach 1 — Inorder Traversal (O(n) time, O(n) space)
Collect all nodes via inorder traversal into a list (sorted order).
Find `p` in the list and return the next/previous element.
Simple but doesn't exploit BST structure.

### Approach 2 — BST Property Traversal (O(h) time, O(1) space)

**Successor:**
- If `p.val < node.val` → node is a candidate successor; go **left** for a closer one.
- If `p.val >= node.val` → successor must be in the right subtree; go **right**.

**Predecessor:**
- If `p.val > node.val` → node is a candidate predecessor; go **right** for a closer one.
- If `p.val <= node.val` → predecessor must be in the left subtree; go **left**.

---

## Key Insight
Successor = leftmost node in the right subtree (if it exists), OR the nearest ancestor
for which the target node lies in its left subtree.
The BST traversal approach captures both cases in a single pass without needing parent
pointers.

---

## Complexity
| Approach          | Time | Space |
|-------------------|------|-------|
| Inorder traversal | O(n) | O(n)  |
| BST traversal     | O(h) | O(1)  |

---

## Edge Cases
- `p` is the maximum node → no successor, return `None`.
- `p` is the minimum node → no predecessor, return `None`.
- `p` is the root → successor is leftmost in right subtree; predecessor is rightmost in left subtree.
- Single-node tree → both successor and predecessor are `None`.
- `p` not in tree → the BST traversal still returns the correct logical successor/predecessor.
