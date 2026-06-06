# Merge Two BSTs into a Balanced BST

## Problem Statement
Given the roots of two BSTs, merge them into a single **height-balanced** BST
containing all elements from both trees.

**Example:**
- BST1 = [3,1,5], BST2 = [4,2,6]
- Output: balanced BST with inorder [1,2,3,4,5,6]

---

## Approach — Inorder + Merge + Build (O(m+n) time, O(m+n) space)

Three steps:

1. **Extract sorted arrays**: Inorder traversal of a BST yields a sorted array.
   Run inorder on both trees → two sorted arrays of sizes m and n.

2. **Merge sorted arrays**: Standard two-pointer merge (like merge sort's merge step)
   combines them into one sorted array of size m+n in O(m+n).

3. **Build balanced BST**: Recursively pick the middle element of the sorted array
   as the root. Left half becomes the left subtree, right half becomes the right subtree.
   This guarantees height balance (same strategy as "Convert Sorted Array to BST").

---

## Key Insight
Inorder traversal of a BST is always sorted. This lets us reduce the problem to:
merge two sorted arrays (classic) + build balanced BST from sorted array (classic).
Neither step requires understanding BST structure beyond inorder traversal.

---

## Complexity
| Step              | Time     | Space    |
|-------------------|----------|----------|
| Inorder both      | O(m+n)   | O(m+n)   |
| Merge arrays      | O(m+n)   | O(m+n)   |
| Build balanced    | O(m+n)   | O(m+n)   |
| **Total**         | O(m+n)   | O(m+n)   |

---

## Edge Cases
- One tree is empty → return the other tree (rebuilt as balanced).
- Both trees empty → return `None`.
- Duplicate values across trees → handled naturally; both are included.
- One tree is a single node → merges correctly into the other tree's sorted sequence.
- Already balanced inputs → output is still rebuilt from scratch as balanced.
