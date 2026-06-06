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
    ## 144. Binary Tree Preorder Traversal

    Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

    ### Examples

    ```text
    Input:  root = [1, null, 2, 3]
    Output: [1, 2, 3]

    Input:  root = []
    Output: []

    Input:  root = [1]
    Output: [1]
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`
    """

    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), Space: O(n)
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive pre-order: root, left subtree, right subtree
        # Time: O(n), Space: O(n)
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


if __name__ == '__main__':
    s = Solution()

    assert s.preorderTraversal(build_tree([1, None, 2, 3])) == [1, 2, 3]
    assert s.preorderTraversal_recursive(build_tree([1, None, 2, 3])) == [1, 2, 3]

    assert s.preorderTraversal(None) == []
    assert s.preorderTraversal(build_tree([1])) == [1]

    print("All tests passed.")
