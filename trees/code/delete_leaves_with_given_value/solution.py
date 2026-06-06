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


def tree_to_list(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    """
    ## 1325. Delete Leaves With a Given Value

    Given a binary tree `root` and an integer `target`, delete all the **leaf nodes** with
    value `target`.

    Note that once you delete a leaf node with value `target`, if its parent node becomes a
    leaf node and has the value `target`, it should also be deleted (you need to continue
    doing this until you can't).

    ---

    ### Examples

    ```text
    Example 1:
        Input:  root = [1, 2, 3, 2, null, 2, 4], target = 2
        Output: [1, null, 3, null, 4]
        Explanation: Leaf nodes with value 2 are removed. Node 2 (left child of root)
                     then becomes a leaf with value 2 and is also removed.

    Example 2:
        Input:  root = [1, 3, 3, 3, 2], target = 3
        Output: [1, 3, null, null, 2]

    Example 3:
        Input:  root = [1, 2, null, 2, null, 2], target = 2
        Output: [1]
    ```

    ---

    ### Constraints

    - The number of nodes in the tree is in the range [1, 3000].
    - 1 <= Node.val, target <= 1000
    """

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:  # O(n) time, O(h) space
        # Post-order: process children first, then check if current node became a leaf with target value
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root


if __name__ == '__main__':
    s = Solution()

    root1 = build_tree([1, 2, 3, 2, None, 2, 4])
    assert tree_to_list(s.removeLeafNodes(root1, 2)) == [1, None, 3, None, 4]

    root2 = build_tree([1, 3, 3, 3, 2])
    assert tree_to_list(s.removeLeafNodes(root2, 3)) == [1, 3, None, None, 2]

    root3 = build_tree([1, 2, None, 2, None, 2])
    assert tree_to_list(s.removeLeafNodes(root3, 2)) == [1]

    print("All tests passed.")
