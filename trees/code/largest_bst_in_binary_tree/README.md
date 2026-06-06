# LC 333 — Largest BST Subtree

## Problem Statement
Given the root of a binary tree, find the largest subtree that is also a valid BST,
and return its size (number of nodes).

**Example:**
- Input: root = [10,5,15,1,8,null,7]
- Output: 3 (subtree rooted at 5: [5,1,8] is a valid BST)

**Constraints:** Number of nodes in [0, 10^4], -10^4 ≤ val ≤ 10^4.

---

## Approaches

### Approach 1 — Check Each Subtree (O(n²) time, O(n) space)
For every node, validate whether the subtree rooted there is a BST (O(n) per node).
Track the maximum valid size seen. Total: O(n²).
Simple but redundant — inner nodes are validated multiple times.

### Approach 2 — Bottom-up Post-order (O(n) time, O(n) space)
Each node returns a tuple `(is_bst, size, min_val, max_val)` to its parent:
- `is_bst`: whether this subtree is a valid BST.
- `size`: number of nodes in this subtree.
- `min_val`: minimum value in this subtree.
- `max_val`: maximum value in this subtree.

A node forms a valid BST if:
1. Both left and right subtrees are valid BSTs.
2. `left.max_val < node.val < right.min_val`.

Update global `max_size` whenever a valid BST is found.
Each node is visited exactly once → O(n).

---

## Key Insight
Post-order traversal lets each node gather complete information from its children
before deciding if it forms a valid BST. By propagating `(is_bst, size, min, max)`
upward, we avoid redundant subtree checks entirely.

---

## Complexity
| Approach       | Time  | Space |
|----------------|-------|-------|
| Naive O(n²)    | O(n²) | O(n)  |
| Bottom-up      | O(n)  | O(n)  |

---

## Edge Cases
- Empty tree → return 0.
- Single node → always a valid BST of size 1.
- Entire tree is a valid BST → return total node count.
- All nodes violate BST property → each leaf is a BST of size 1; return 1.
- Duplicate values → a valid BST requires strict inequality; duplicates make it invalid.
- Left subtree is valid BST but right is not → only left subtree size counts.
