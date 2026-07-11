"""
# LC 100: Same Tree

Given the roots of two binary trees, return true if they are structurally identical and
the nodes have the same values.

## Examples
```text
Input:  p = [1, 2, 3], q = [1, 2, 3]
Output: true

Input:  p = [1, 2], q = [1, null, 2]
Output: false

Input:  p = [1, 2, 1], q = [1, 1, 2]
Output: false
```

## Constraints
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
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
    ## 100. Same Tree

    Given the roots of two binary trees `p` and `q`, write a function to check if they
    are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the
    nodes have the same value.

    ### Examples

    ```text
    Input:  p = [1, 2, 3], q = [1, 2, 3]
    Output: true

    Input:  p = [1, 2], q = [1, null, 2]
    Output: false

    Input:  p = [1, 2, 1], q = [1, 1, 2]
    Output: false
    ```

    ### Constraints

    - The number of nodes in both trees is in the range `[0, 100]`.
    - `-10^4 <= Node.val <= 10^4`
    """

    def isSameTree_recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time: O(n), Space: O(n)
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree_recursive(p.left, q.left) and self.isSameTree_recursive(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both None: same; one None: different; values differ: different
        # Recursively check left and right subtrees
        # Time: O(n), Space: O(n)
        queue = deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True


if __name__ == '__main__':
    s = Solution()

    assert s.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert s.isSameTree_recursive(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True

    assert s.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert s.isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
    assert s.isSameTree(None, None) is True

    print("All tests passed.")
