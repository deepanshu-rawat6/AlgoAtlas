"""
# LC 98: Validate Binary Search Tree

Determine if a binary tree is a valid BST: the left subtree contains only values
strictly less than the node, the right subtree only strictly greater, recursively.

## Examples
```text
Input:  root = [2, 1, 3]
Output: true

Input:  root = [5, 1, 4, null, null, 3, 6]
Output: false
```

## Constraints
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
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
    ## 98. Validate Binary Search Tree

    Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys **less than** the node's key.
    - The right subtree of a node contains only nodes with keys **greater than** the node's key.
    - Both the left and right subtrees must also be binary search trees.

    ---

    ### Examples

    ```text
    Example 1:
        Input:  root = [2, 1, 3]
        Output: true

    Example 2:
        Input:  root = [5, 1, 4, null, null, 3, 6]
        Output: false
        Explanation: The root node's value is 5, but its right child's value is 4.
    ```

    ---

    ### Constraints

    - The number of nodes in the tree is in the range [1, 10^4].
    - -2^31 <= Node.val <= 2^31 - 1
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:  # O(n) time, O(h) space
        # Pass valid range [lo, hi] down; each node must be strictly within range
        # Going left tightens upper bound; going right tightens lower bound
        def validate(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

        return validate(root, float('-inf'), float('inf'))

    def isValidBST_inorder(self, root: Optional[TreeNode]) -> bool:  # O(n) time, O(n) space
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return all(result[i] < result[i + 1] for i in range(len(result) - 1))


if __name__ == '__main__':
    s = Solution()

    root1 = build_tree([2, 1, 3])
    assert s.isValidBST(root1) == True
    assert s.isValidBST_inorder(build_tree([2, 1, 3])) == True

    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    assert s.isValidBST(root2) == False
    assert s.isValidBST_inorder(build_tree([5, 1, 4, None, None, 3, 6])) == False

    root3 = build_tree([2, 2, 2])
    assert s.isValidBST(root3) == False

    print("All tests passed.")
