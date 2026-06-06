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
    ## 104. Maximum Depth of Binary Tree

    Given the `root` of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.

    ### Examples

    ```text
    Input:  root = [3, 9, 20, null, null, 15, 7]
    Output: 3

    Input:  root = [1, null, 2]
    Output: 2
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-100 <= Node.val <= 100`
    """

    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), Space: O(n)
        if not root:
            return 0
        return 1 + max(self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Depth = 1 + max(depth of left, depth of right); base case is None -> 0
        # Time: O(n), Space: O(n)
        if not root:
            return 0
        depth, queue = 0, deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


if __name__ == '__main__':
    s = Solution()

    assert s.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert s.maxDepth_recursive(build_tree([3, 9, 20, None, None, 15, 7])) == 3

    assert s.maxDepth(build_tree([1, None, 2])) == 2
    assert s.maxDepth(None) == 0

    print("All tests passed.")
