"""
# LC 105: Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal arrays of a binary tree (all values unique),
reconstruct and return the tree.

## Examples
```text
Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]

Input:  preorder = [-1], inorder = [-1]
Output: [-1]
```

## Constraints
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- preorder and inorder consist of unique values.
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(vals):
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


def tree_to_list(root):
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
    ## 105. Construct Binary Tree from Preorder and Inorder Traversal

    Given two integer arrays `preorder` and `inorder` where:
    - `preorder` is the preorder traversal of a binary tree, and
    - `inorder` is the inorder traversal of the same tree,

    construct and return the binary tree.

    ---

    ### Examples

    ```text
    Example 1:
        Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
        Output: [3, 9, 20, null, null, 15, 7]

    Example 2:
        Input:  preorder = [-1], inorder = [-1]
        Output: [-1]
    ```

    ---

    ### Constraints

    - 1 <= preorder.length <= 3000
    - inorder.length == preorder.length
    - -3000 <= preorder[i], inorder[i] <= 3000
    - `preorder` and `inorder` consist of unique values.
    - Each value of `inorder` also appears in `preorder`.
    - `preorder` is guaranteed to be the preorder traversal of the tree.
    - `inorder` is guaranteed to be the inorder traversal of the tree.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  # O(n^2) time, O(n) space
        # Preorder[0] is always the root; find it in inorder to split left/right
        # Left subtree has len(left_inorder) nodes in preorder; recurse on both halves
        if not preorder:
            return None
        root_val = preorder[0]
        mid = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

    def buildTree_hashmap(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  # O(n) time, O(n) space
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = idx_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    s = Solution()

    pre, ino = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    assert tree_to_list(s.buildTree(pre, ino)) == [3, 9, 20, None, None, 15, 7]
    assert tree_to_list(s.buildTree_hashmap(pre, ino)) == [3, 9, 20, None, None, 15, 7]

    pre2, ino2 = [-1], [-1]
    assert tree_to_list(s.buildTree(pre2, ino2)) == [-1]
    assert tree_to_list(s.buildTree_hashmap(pre2, ino2)) == [-1]

    print("All tests passed.")
