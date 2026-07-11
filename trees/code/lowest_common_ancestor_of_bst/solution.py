"""
# LC 235: Lowest Common Ancestor of a Binary Search Tree

Find the lowest common ancestor (LCA) of two nodes p and q in a BST. The LCA is the
deepest node that has both p and q as descendants (a node is a descendant of itself).

## Examples
```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
Output: 6

Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
Output: 2
```

## Constraints
- The number of nodes in the tree is in the range [2, 10^5].
- All Node.val are unique; p and q exist in the BST.
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


class Solution:
    """
    ## 235. Lowest Common Ancestor of a Binary Search Tree

    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given
    nodes in the BST.

    The LCA is defined as the lowest node in the tree that has both `p` and `q` as descendants
    (a node can be a descendant of itself).

    ### Examples

    ```text
    Example 1:
    Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6

    Example 2:
    Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2

    Example 3:
    Input:  root = [2,1], p = 2, q = 1
    Output: 2
    ```

    ### Constraints
    - The number of nodes in the tree is in the range `[2, 10^5]`.
    - `-10^9 <= Node.val <= 10^9`
    - All `Node.val` are unique.
    - `p != q`
    - `p` and `q` will exist in the BST.
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # In BST: if both p,q < root go left; if both > root go right; else root is LCA
        # Time: O(h), Space: O(h) — recurse toward the split point using BST property
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def lowestCommonAncestor_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(h), Space: O(1) — walk down without recursion stack
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


if __name__ == '__main__':
    sol = Solution()

    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p, q = find_node(root, 2), find_node(root, 8)
    assert sol.lowestCommonAncestor(root, p, q).val == 6
    assert sol.lowestCommonAncestor_iterative(root, p, q).val == 6

    p2, q2 = find_node(root, 2), find_node(root, 4)
    assert sol.lowestCommonAncestor(root, p2, q2).val == 2
    assert sol.lowestCommonAncestor_iterative(root, p2, q2).val == 2

    print("All tests passed.")
