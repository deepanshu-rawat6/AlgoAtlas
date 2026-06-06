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
    ## 124. Binary Tree Maximum Path Sum

    A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in
    the sequence has an edge connecting them. A node can only appear in the sequence **at most
    once**. Note that the path does not need to pass through the root.

    The **path sum** of a path is the sum of the node's values in the path.

    Given the `root` of a binary tree, return the maximum path sum of any **non-empty** path.

    ---

    ### Examples

    ```text
    Example 1:
        Input:  root = [1, 2, 3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

    Example 2:
        Input:  root = [-10, 9, 20, null, null, 15, 7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    ```

    ---

    ### Constraints

    - The number of nodes in the tree is in the range [1, 3 * 10^4].
    - -1000 <= Node.val <= 1000
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:  # O(n) time, O(h) space
        # For each node, max path through it = node.val + max(0, left) + max(0, right)
        # Update global max; return node.val + max(0, best single branch) to parent
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum


if __name__ == '__main__':
    s = Solution()

    root1 = build_tree([1, 2, 3])
    assert s.maxPathSum(root1) == 6

    root2 = build_tree([-10, 9, 20, None, None, 15, 7])
    assert s.maxPathSum(root2) == 42

    root3 = build_tree([-3])
    assert s.maxPathSum(root3) == -3

    print("All tests passed.")
