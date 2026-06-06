# LC 1008 — Construct BST from Preorder Traversal

## Problem Statement
Given an array of integers `preorder` representing the preorder traversal of a BST,
construct and return the BST.

**Example:**
- Input: preorder = [8,5,1,7,10,12]
- Output: [8,5,10,1,7,null,12]

**Constraints:** 1 ≤ preorder.length ≤ 100, all values are unique.

---

## Approaches

### Approach 1 — Recursive with Upper Bound (O(n) time, O(n) space)
Use a global index and an `upper` bound parameter:
- The first element is always the root.
- For the left subtree, the upper bound is the root's value (left children must be smaller).
- For the right subtree, the upper bound is inherited from the parent.
- Stop recursing when the current element exceeds the upper bound.

This processes each element exactly once → O(n).

### Approach 2 — Stack-based (O(n) time, O(n) space)
Maintain a stack of nodes processed so far:
- If the new value is **less** than the stack top → it's the left child of the top.
- Otherwise, **pop** until the stack top is greater than the new value; the last popped
  node is the parent, and the new node becomes its right child.

Mimics the recursive call stack explicitly.

---

## Key Insight
In preorder traversal, the first element is always the root. For the left subtree,
all values must be less than the root — so we keep consuming elements as long as
they are below the current node's upper bound. The moment a value exceeds the bound,
we backtrack and attach it to the right.

---

## Complexity
| Approach          | Time | Space |
|-------------------|------|-------|
| Recursive bounds  | O(n) | O(n)  |
| Stack-based       | O(n) | O(n)  |

---

## Edge Cases
- Single element → tree with just the root.
- Sorted ascending input → right-skewed tree (each element is right child of previous).
- Sorted descending input → left-skewed tree.
- All elements equal → not possible per constraints (values are unique).
