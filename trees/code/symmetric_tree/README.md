# Symmetric Tree (LC 101)

Check whether a binary tree is a mirror of itself (symmetric around its center).

## Approaches

### Recursive (Mirror Check)
- **Time:** O(n), **Space:** O(h)
- Check if the left and right subtrees are mirrors: `is_mirror(left, right)`. Two subtrees are mirrors if their roots have equal values, and `left.left` mirrors `right.right` (outer pair) and `left.right` mirrors `right.left` (inner pair).

### Iterative BFS with Mirror Pairs
- **Time:** O(n), **Space:** O(n)
- Use a queue of `(left, right)` pairs. For each pair: both None → continue; one None or values differ → `False`; otherwise enqueue `(left.left, right.right)` and `(left.right, right.left)`.

## Key Insight

Symmetry means the tree is its own mirror image. The key is comparing mirror positions: the outer pair (`left.left` vs `right.right`) and the inner pair (`left.right` vs `right.left`). This is different from comparing left subtree to right subtree directly — it's a cross-comparison.

## Edge Cases

- Single node → symmetric (trivially).
- `[1, 2, 2, null, 3, null, 3]` → not symmetric (inner nodes differ from outer).
- All same values → symmetric only if structure is also symmetric.
