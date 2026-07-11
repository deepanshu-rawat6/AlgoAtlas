"""
# LC 199: Binary Tree Right Side View

Return the values of nodes visible when looking at the tree from the right side,
ordered top to bottom.

## Examples
```text
Input:  root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Input:  root = [1, null, 3]
Output: [1, 3]

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


class Solution:
    """
    ## 199. Binary Tree Right Side View

    Given the `root` of a binary tree, imagine yourself standing on the right side of it.
    Return the values of the nodes you can see ordered from top to bottom.

    ### Examples

    ```text
    Example 1:
    Input:  root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

    Example 2:
    Input:  root = [1,null,3]
    Output: [1,3]

    Example 3:
    Input:  root = []
    Output: []
    ```

    ### Constraints
    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS level by level; the last node in each level is visible from the right
        # Time: O(n), Space: O(n) — take the last node of each BFS level
        if not root:
            return []
        result, queue = [], deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), Space: O(h) — visit right child first; first visit at each depth is visible
        result = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(result):
                result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


if __name__ == '__main__':
    sol = Solution()

    root = build_tree([1, 2, 3, None, 5, None, 4])
    assert sol.rightSideView(root) == [1, 3, 4]
    assert sol.rightSideView_dfs(root) == [1, 3, 4]

    root2 = build_tree([1, None, 3])
    assert sol.rightSideView(root2) == [1, 3]
    assert sol.rightSideView_dfs(root2) == [1, 3]

    assert sol.rightSideView(None) == []

    print("All tests passed.")
