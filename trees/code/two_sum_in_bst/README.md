# LC 653 — Two Sum IV (Input is a BST)

## Problem Statement
Given the root of a BST and an integer `k`, return `True` if there exist two elements
in the BST such that their sum equals `k`, otherwise return `False`.

**Example:**
- root = [5,3,6,2,4,null,7], k = 9
- Output: True (2 + 7 = 9)

**Constraints:** Number of nodes in [1, 10^4], -10^4 ≤ val ≤ 10^4, k is unique.

---

## Approaches

### Approach 1 — Inorder + Two Pointers (O(n) time, O(n) space)
1. Collect all values via inorder traversal → sorted array.
2. Apply classic two-pointer technique: `lo` at start, `hi` at end.
   - Sum < k → move `lo` right (need larger value).
   - Sum > k → move `hi` left (need smaller value).
   - Sum == k → return `True`.

Leverages BST's sorted inorder property directly.

### Approach 2 — DFS + Hash Set (O(n) time, O(n) space)
Traverse the tree (any order). For each node with value `v`, check if `k - v`
is already in a hash set. If yes, return `True`. Otherwise, add `v` to the set.

Works on any binary tree, not just BSTs. Slightly simpler to implement.

---

## Key Insight
BST inorder gives a sorted array for free, enabling the O(n) two-pointer approach
without sorting. The hash set approach is more general but loses the BST advantage.

---

## Complexity
| Approach          | Time | Space |
|-------------------|------|-------|
| Inorder + 2ptr    | O(n) | O(n)  |
| DFS + hash set    | O(n) | O(n)  |

---

## Edge Cases
- Single node → can't form a pair, return `False`.
- k equals twice a node's value → need two distinct nodes; a node can't pair with itself.
- All nodes have the same value → only valid if k == 2*val and there are ≥ 2 nodes.
- Negative values → both approaches handle naturally.
- k larger than sum of two largest → return `False`.
