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
    ## 337. House Robber III

    The thief has found himself a new place for his thievery again. There is only one entrance
    to this area, called `root`.

    Besides the root, each house has one and only one parent house. After a tour, the smart
    thief realized that all houses in this place form a binary tree. It will automatically
    contact the police if **two directly-linked houses were broken into on the same night**.

    Given the `root` of the binary tree, return the maximum amount of money the thief can rob
    **without alerting the police**.

    ---

    ### Examples

    ```text
    Example 1:
        Input:  root = [3, 2, 3, null, 3, null, 1]
        Output: 7
        Explanation: Rob node 3 (root) + node 3 (left-right) + node 1 (right-right) = 3 + 3 + 1 = 7.

    Example 2:
        Input:  root = [3, 4, 5, 1, 3, null, 1]
        Output: 9
        Explanation: Rob node 4 (left) + node 5 (right) = 4 + 5 = 9.
    ```

    ---

    ### Constraints

    - The number of nodes in the tree is in the range [1, 10^4].
    - 0 <= Node.val <= 10^4
    """

    def rob(self, root: Optional[TreeNode]) -> int:  # O(n) time, O(n) space
        # For each node return (rob_this, skip_this) pair
        # rob_this = node.val + skip_left + skip_right
        # skip_this = max(rob_left, skip_left) + max(rob_right, skip_right)
        memo = {}

        def dfs(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            # rob this node: skip children, take grandchildren
            rob_this = node.val
            if node.left:
                rob_this += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_this += dfs(node.right.left) + dfs(node.right.right)
            skip_this = dfs(node.left) + dfs(node.right)
            memo[node] = max(rob_this, skip_this)
            return memo[node]

        return dfs(root)

    def rob_pair(self, root: Optional[TreeNode]) -> int:  # O(n) time, O(h) space
        def dfs(node):
            # returns (max if rob node, max if skip node)
            if not node:
                return (0, 0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            rob_this = node.val + left_skip + right_skip
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            return (rob_this, skip_this)

        return max(dfs(root))


if __name__ == '__main__':
    s = Solution()

    root1 = build_tree([3, 2, 3, None, 3, None, 1])
    assert s.rob(root1) == 7
    assert s.rob_pair(build_tree([3, 2, 3, None, 3, None, 1])) == 7

    root2 = build_tree([3, 4, 5, 1, 3, None, 1])
    assert s.rob(root2) == 9
    assert s.rob_pair(build_tree([3, 4, 5, 1, 3, None, 1])) == 9

    print("All tests passed.")
