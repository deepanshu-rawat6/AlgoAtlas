# LC 700 — Search in a Binary Search Tree

## Problem Statement
Given the root of a BST and an integer `val`, find the node whose value equals `val`
and return the subtree rooted at that node. If no such node exists, return `None`.

**Example:**
- Input: root = [4,2,7,1,3], val = 2
- Output: [2,1,3]

**Constraints:** Number of nodes in [1, 5000], 1 ≤ val ≤ 10^7, BST is valid.

---

## Approaches

### Approach 1 — Recursive (O(h) time, O(h) space)
At each node, compare `val` with `node.val`:
- Equal → return the node.
- Less → recurse into left subtree.
- Greater → recurse into right subtree.

The call stack depth equals the tree height h (O(log n) balanced, O(n) worst).

### Approach 2 — Iterative (O(h) time, O(1) space)
Same logic as recursive but uses a `while` loop and moves the pointer.
Preferred in practice: no stack overhead, constant extra space.

---

## Key Insight
BST property eliminates half the search space at every node — exactly like binary
search on a sorted array. You never need to explore both subtrees.

---

## Complexity
| Approach   | Time  | Space |
|------------|-------|-------|
| Recursive  | O(h)  | O(h)  |
| Iterative  | O(h)  | O(1)  |

h = O(log n) for balanced BST, O(n) for skewed.

---

## Edge Cases
- `val` not present in the tree → return `None`.
- `val` equals the root value → return root immediately.
- Single-node tree → works correctly for both match and no-match.
- Left-skewed or right-skewed tree → degrades to O(n) but still correct.
- `val` smaller than all nodes → traverses entirely to the left, returns `None`.
