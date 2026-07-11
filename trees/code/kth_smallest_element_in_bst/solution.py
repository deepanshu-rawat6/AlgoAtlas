"""
# LC 230: Kth Smallest Element in a BST

Return the k-th smallest value (1-indexed) in a BST.

## Examples
```text
Input:  root = [3, 1, 4, null, 2], k = 1
Output: 1

Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
Output: 3
```

## Constraints
- The number of nodes in the tree is n, with 1 <= k <= n <= 10^4.
- 0 <= Node.val <= 10^4
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


class Solution:
    """
    ## 230. Kth Smallest Element in a BST

    Given the `root` of a binary search tree, and an integer `k`, return the
    `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

    ---

    ### Examples

    ```text
    Example 1:
        Input:  root = [3, 1, 4, null, 2], k = 1
        Output: 1

    Example 2:
        Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
        Output: 3
    ```

    ---

    ### Constraints

    - The number of nodes in the tree is `n`.
    - 1 <= k <= n <= 10^4
    - 0 <= Node.val <= 10^4
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  # O(n) time, O(n) space
        # In-order traversal of BST yields sorted order; return the k-th element
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result[k - 1]

    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:  # O(h+k) time, O(h) space
        stack = []
        node = root
        count = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
        return -1


if __name__ == '__main__':
    s = Solution()

    root1 = build_tree([3, 1, 4, None, 2])
    assert s.kthSmallest(root1, 1) == 1
    assert s.kthSmallest_iterative(build_tree([3, 1, 4, None, 2]), 1) == 1

    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert s.kthSmallest(root2, 3) == 3
    assert s.kthSmallest_iterative(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3

    print("All tests passed.")
