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
    ## 543. Diameter of Binary Tree

    Given the `root` of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes
    in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

    ### Examples

    ```text
    Input:  root = [1, 2, 3, 4, 5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    Input:  root = [1, 2]
    Output: 1
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-100 <= Node.val <= 100`
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # For each node, diameter through it = left_height + right_height
        # Track global max; return height (1 + max child height) up the recursion
        # Time: O(n), Space: O(n)
        self.diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter


if __name__ == '__main__':
    s = Solution()

    assert s.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3
    assert s.diameterOfBinaryTree(build_tree([1, 2])) == 1
    assert s.diameterOfBinaryTree(build_tree([1])) == 0

    print("All tests passed.")
