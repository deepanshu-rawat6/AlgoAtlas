# Balanced Binary Tree (LC 110)

Determine if a binary tree is height-balanced: every node's left and right subtrees differ in height by at most 1.

## Approaches

### Top-Down (naive)
- **Time:** O(n²), **Space:** O(n)
- For each node, compute heights of both subtrees and check the difference. Recurse on both children. Recomputes heights repeatedly.

### Bottom-Up DFS (optimal)
- **Time:** O(n), **Space:** O(h)
- A helper returns the height if the subtree is balanced, or `-1` if it's not. At each node: get left and right heights; if either is `-1` or heights differ by > 1, return `-1`. Otherwise return `1 + max(left, right)`. The `-1` sentinel propagates upward immediately, short-circuiting the traversal.

## Key Insight

The bottom-up approach avoids recomputing heights by combining the height calculation and balance check into a single pass. The `-1` sentinel is the key: once an imbalance is detected anywhere in the tree, it bubbles up without any further work.

## Edge Cases

- Empty tree → balanced (return `True`).
- Single node → balanced.
- A tree that is balanced at the root but has an imbalanced subtree deep inside → bottom-up catches it and returns `-1` immediately.
