"""
# LC 102: Binary Tree Level Order Traversal

Return the level-order traversal of a binary tree as a list of lists (one list per
level, left to right).

## Examples
```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

Input:  root = [1]
Output: [[1]]

Input:  root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
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
    ## 102. Binary Tree Level Order Traversal

    Given the `root` of a binary tree, return the level order traversal of its nodes' values
    (i.e., from left to right, level by level).

    ### Examples

    ```text
    Example 1:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:
    Input:  root = [1]
    Output: [[1]]

    Example 3:
    Input:  root = []
    Output: []
    ```

    ### Constraints
    - The number of nodes in the tree is in the range `[0, 2000]`.
    - `-1000 <= Node.val <= 1000`
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS with a queue; process all nodes at current level before moving to next
        # Time: O(n), Space: O(n) — process nodes level by level using a queue
        if not root:
            return []
        result, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def levelOrder_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS with depth index; extend result list when reaching a new depth level
        # Time: O(n), Space: O(n) — use recursion depth as level index
        result = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(result):
                result.append([])
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result


if __name__ == '__main__':
    sol = Solution()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert sol.levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrder_dfs(root) == [[3], [9, 20], [15, 7]]

    assert sol.levelOrder(build_tree([1])) == [[1]]
    assert sol.levelOrder(None) == []

    print("All tests passed.")
