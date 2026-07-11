"""
# LC 226: Invert Binary Tree

Invert a binary tree (mirror it) and return its root.

## Examples
```text
Input:  root = [4, 2, 7, 1, 3, 6, 9]
Output: [4, 7, 2, 9, 6, 3, 1]

Input:  root = [2, 1, 3]
Output: [2, 3, 1]

Input:  root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
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


def tree_to_list(root: Optional[TreeNode]) -> List:
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    """
    ## 226. Invert Binary Tree

    Given the `root` of a binary tree, invert the tree, and return its root.

    ### Examples

    ```text
    Input:  root = [4, 2, 7, 1, 3, 6, 9]
    Output: [4, 7, 2, 9, 6, 3, 1]

    Input:  root = [2, 1, 3]
    Output: [2, 3, 1]

    Input:  root = []
    Output: []
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`
    """

    def invertTree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n), Space: O(n)
        if not root:
            return None
        root.left, root.right = self.invertTree_recursive(root.right), self.invertTree_recursive(root.left)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Swap left and right children, then recursively invert both subtrees
        # Time: O(n), Space: O(n)
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


if __name__ == '__main__':
    s = Solution()

    assert tree_to_list(s.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(s.invertTree_recursive(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert s.invertTree(None) is None

    print("All tests passed.")
