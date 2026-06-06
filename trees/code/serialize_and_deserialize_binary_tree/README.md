# Serialize and Deserialize Binary Tree (LC 297)

Design an algorithm to convert a binary tree to a string and reconstruct the original tree from that string.

## Approaches

### BFS Level-Order
- **Time:** O(n), **Space:** O(n)
- Serialize: BFS, encode each node's value; encode `None` children as `"null"`. Join with commas.
- Deserialize: split tokens, reconstruct using a queue of parent nodes. Assign left and right children from the token stream in order.

### DFS Preorder
- **Time:** O(n), **Space:** O(n)
- Serialize: preorder DFS, encode `None` as `"null"`.
- Deserialize: use an iterator over tokens. Recursively build: if token is `"null"` return `None`; otherwise create a node and recurse for left then right.

## Key Insight

Both approaches encode `None` nodes explicitly to preserve structural information. Without encoding `None`, you can't distinguish between different tree shapes with the same values. The DFS approach is elegant because the preorder structure directly mirrors the recursive reconstruction — the first token is always the root, and the subtree boundaries are implicit in the `null` markers.

## Edge Cases

- Empty tree → serialize to `""` / `"null"`, deserialize back to `None`.
- Single node → `"1,null,null"` (DFS) or `"1"` (BFS).
- Tree with negative values → string conversion handles negatives correctly.
