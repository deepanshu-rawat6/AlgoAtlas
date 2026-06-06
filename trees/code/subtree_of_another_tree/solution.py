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
    ## 572. Subtree of Another Tree

    Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree
    of `root` with the same structure and node values as `subRoot`, and `false` otherwise.

    A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of
    this node's descendants. The tree `tree` could also be considered as a subtree of itself.

    ### Examples

    ```text
    Example 1:
    Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Example 2:
    Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false
    ```

    ### Constraints
    - The number of nodes in the `root` tree is in the range `[1, 2000]`.
    - The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
    - `-10^4 <= root.val, subRoot.val <= 10^4`
    """

    def _is_same(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return self._is_same(s.left, t.left) and self._is_same(s.right, t.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check if root itself matches subRoot, or if subRoot is in either subtree
        # Time: O(m*n), Space: O(m) — check every node in root against subRoot
        if not root:
            return False
        if self._is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == '__main__':
    sol = Solution()

    root1 = build_tree([3, 4, 5, 1, 2])
    sub1 = build_tree([4, 1, 2])
    assert sol.isSubtree(root1, sub1) == True

    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub2 = build_tree([4, 1, 2])
    assert sol.isSubtree(root2, sub2) == False

    assert sol.isSubtree(None, build_tree([1])) == False

    print("All tests passed.")
