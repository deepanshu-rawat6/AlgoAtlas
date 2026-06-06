# Floor and Ceil in a BST

## Problem Statement
Given a BST and a target key:
- **Floor**: largest value in the BST that is ≤ key.
- **Ceil**: smallest value in the BST that is ≥ key.

Return -1 if no floor/ceil exists.

**Example:**
- BST = [8,4,12,2,6,10,14], key = 5
- Floor = 4, Ceil = 6

---

## Approach — Iterative Candidate Tracking (O(h) time, O(1) space)

### Floor
Traverse the BST keeping a `floor_val` candidate:
- If `node.val == key` → exact match, return immediately.
- If `node.val < key` → node is a valid floor candidate (update `floor_val`), go **right**
  to look for a closer (larger) value still ≤ key.
- If `node.val > key` → too large, go **left**.

### Ceil
Mirror logic with a `ceil_val` candidate:
- If `node.val == key` → exact match, return immediately.
- If `node.val > key` → node is a valid ceil candidate (update `ceil_val`), go **left**
  to look for a closer (smaller) value still ≥ key.
- If `node.val < key` → too small, go **right**.

---

## Key Insight
When you move **right** (because current < key), the current node becomes a floor
candidate — it's the largest value seen so far that is still ≤ key.
When you move **left** (because current > key), the current node becomes a ceil
candidate — it's the smallest value seen so far that is still ≥ key.

---

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Floor     | O(h) | O(1)  |
| Ceil      | O(h) | O(1)  |

---

## Edge Cases
- Key smaller than all nodes → floor = -1, ceil = smallest node.
- Key larger than all nodes → floor = largest node, ceil = -1.
- Key exactly in tree → floor = ceil = key.
- Empty tree → both return -1.
- Single-node tree → floor or ceil equals that node's value if it satisfies the condition.
