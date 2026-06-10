# LC 1214 — Two Sum BSTs

## Problem Statement
Given the roots of **two BSTs** and an integer `target`, return `True` if there exists
a node in the first tree and a node in the second tree such that their values sum to `target`.

**Example:**
- root1 = [2,1,4], root2 = [1,0,3], target = 5
- Output: True (2 from tree1 + 3 from tree2 = 5)

**Constraints:** Each tree has [1, 5000] nodes, -10^9 ≤ val ≤ 10^9, -10^9 ≤ target ≤ 10^9.

---

## Approaches

### Approach 1 — Inorder + Two Pointers (O(n+m) time, O(n+m) space)
1. Collect sorted inorder of tree1 → `l1` (ascending).
2. Collect sorted inorder of tree2 → `l2` (ascending).
3. Two pointers: `i=0` on l1 (left), `j=len(l2)-1` on l2 (right).
   - sum < target → move `i` right (need larger from tree1).
   - sum > target → move `j` left (need smaller from tree2).
   - sum == target → return `True`.

Classic Two Sum II applied across two sorted arrays.

### Approach 2 — DFS + BST Search (O(n·log m) time, O(h1+h2) space)
For each node in tree1, binary-search for `target - node.val` in tree2.
No extra space for storing arrays — exploits BST structure directly.

---

## Key Insight
This is Two Sum split across two BSTs. The inorder approach converts both BSTs into
sorted arrays, reducing it to the classic sorted two-pointer problem. Unlike LC 653
(single BST), you can't use a hash set scan in a single pass — you need two structures.

Related: LC 1 (Two Sum), LC 653 (Two Sum IV - single BST), LC 167 (Two Sum II - sorted array).

---

## Complexity
| Approach              | Time        | Space      |
|-----------------------|-------------|------------|
| Inorder + Two Ptrs    | O(n + m)    | O(n + m)   |
| DFS + BST Search      | O(n · log m)| O(h1 + h2) |

---

## Edge Cases
- target is smaller than min(tree1) + min(tree2) → return `False`.
- target is larger than max(tree1) + max(tree2) → return `False`.
- Single-node trees → check if root1.val + root2.val == target.
- Negative values → handled naturally by both approaches.
