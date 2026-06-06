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
    ## 110. Balanced Binary Tree

    Given a binary tree, determine if it is height-balanced.

    A height-balanced binary tree is a binary tree in which the depth of the two subtrees
    of every node never differs by more than one.

    ### Examples

    ```text
    Input:  root = [3, 9, 20, null, null, 15, 7]
    Output: true

    Input:  root = [1, 2, 2, 3, 3, null, null, 4, 4]
    Output: false

    Input:  root = []
    Output: true
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[0, 5000]`.
    - `-10^4 <= Node.val <= 10^4`
    """

    def isBalanced_topdown(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n^2), Space: O(n)
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return self.isBalanced_topdown(root.left) and self.isBalanced_topdown(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return height if balanced, -1 if not; propagate -1 upward on imbalance
        # A node is balanced if both subtrees are balanced and heights differ by <= 1
        # Time: O(n), Space: O(n)
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


if __name__ == '__main__':
    s = Solution()

    assert s.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])) is True
    assert s.isBalanced_topdown(build_tree([3, 9, 20, None, None, 15, 7])) is True

    assert s.isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert s.isBalanced(None) is True

    print("All tests passed.")
