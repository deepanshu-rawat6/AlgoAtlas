# Insert into a Binary Search Tree (LC 701)

Insert a value into a BST and return the root. The value is guaranteed not to exist in the tree.

## Approaches

### Recursive
- **Time:** O(h), **Space:** O(h)
- If `root` is None, return a new node. If `val < root.val`, recurse left; otherwise recurse right. Return `root` after updating the child.

### Iterative
- **Time:** O(h), **Space:** O(1)
- Walk down the tree following BST ordering. When the appropriate child is None, insert the new node there.

## Key Insight

BST insertion always lands at a leaf position — the BST property uniquely determines the insertion path. There's no need to rebalance (this is a plain BST, not AVL/Red-Black). The recursive approach is clean because returning the (possibly new) node up the call stack naturally wires the new leaf into the tree.

## Edge Cases

- Empty tree → return a single new node.
- Insert smaller than all existing values → goes to the leftmost leaf.
- Insert larger than all existing values → goes to the rightmost leaf.
- The value is guaranteed unique, so no duplicate handling needed.
