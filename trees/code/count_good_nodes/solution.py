"""
# LC 1448: Count Good Nodes in Binary Tree

A node X is "good" if no node on the path from root to X has a value greater than X.
Return the count of good nodes in the tree.

## Examples
```text
Input:  root = [3, 1, 4, 3, null, 1, 5]
Output: 4

Input:  root = [3, 3, null, 4, 2]
Output: 3

Input:  root = [1]
Output: 1
```

## Constraints
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].
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
    ## 1448. Count Good Nodes in Binary Tree

    Given a binary tree `root`, a node X in the tree is named **good** if in the path from root
    to X there are no nodes with a value greater than X.

    Return the number of good nodes in the binary tree.

    ### Examples

    ```text
    Example 1:
    Input:  root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes 3 (root), 3 (left-left), 4 (right), and 5 (right-right) are good.

    Example 2:
    Input:  root = [3,3,null,4,2]
    Output: 3
    Explanation: Nodes 3 (root), 3 (left), and 4 (left-left) are good.

    Example 3:
    Input:  root = [1]
    Output: 1
    ```

    ### Constraints
    - The number of nodes in the binary tree is in the range `[1, 10^5]`.
    - Each node's value is between `[-10^4, 10^4]`.
    """

    def goodNodes(self, root: TreeNode) -> int:
        # A node is 'good' if its value >= max value seen on path from root
        # DFS passing the running max; count good nodes bottom-up
        # Time: O(n), Space: O(h) — DFS tracking the max value seen on the path from root
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if not node:
                return 0
            count = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return count + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)


if __name__ == '__main__':
    sol = Solution()

    root = build_tree([3, 1, 4, 3, None, 1, 5])
    assert sol.goodNodes(root) == 4

    root2 = build_tree([3, 3, None, 4, 2])
    assert sol.goodNodes(root2) == 3

    root3 = build_tree([1])
    assert sol.goodNodes(root3) == 1

    print("All tests passed.")
