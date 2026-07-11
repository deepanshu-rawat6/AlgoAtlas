"""
# LC 94: Binary Tree Inorder Traversal

Return the inorder traversal (left -> root -> right) of a binary tree's node values.

## Examples
```text
Input:  root = [1, null, 2, 3]
Output: [1, 3, 2]

Input:  root = []
Output: []

Input:  root = [1]
Output: [1]
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


class Solution:
    """
    ## 94. Binary Tree Inorder Traversal

    Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

    ### Examples

    ```text
    Input:  root = [1, null, 2, 3]
    Output: [1, 3, 2]

    Input:  root = []
    Output: []

    Input:  root = [1]
    Output: [1]
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`
    """

    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), Space: O(n)
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive in-order: left subtree, root, right subtree
        # Time: O(n), Space: O(n)
        result, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result


if __name__ == '__main__':
    s = Solution()

    root = build_tree([1, None, 2, 3])
    assert s.inorderTraversal(root) == [1, 3, 2]
    assert s.inorderTraversal_recursive(build_tree([1, None, 2, 3])) == [1, 3, 2]

    assert s.inorderTraversal(None) == []
    assert s.inorderTraversal(build_tree([1])) == [1]

    print("All tests passed.")
