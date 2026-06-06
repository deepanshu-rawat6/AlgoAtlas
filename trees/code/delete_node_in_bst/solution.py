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


def tree_to_list(root: Optional[TreeNode]) -> List:
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
    ## 450. Delete Node in a BST

    Given a root node reference of a BST and a key, delete the node with the given key in the BST.
    Return the root node reference (possibly updated) of the BST.

    The deletion can be divided into two stages:
    1. Search for the node to remove.
    2. If the node is found, delete the node.

    ### Examples

    ```text
    Example 1:
    Input:  root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]

    Example 2:
    Input:  root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]

    Example 3:
    Input:  root = [], key = 0
    Output: []
    ```

    ### Constraints
    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-10^5 <= Node.val <= 10^5`
    - Each node has a unique value.
    - `root` is a valid binary search tree.
    - `-10^5 <= key <= 10^5`
    """

    def _find_min(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Find node: go left/right based on key comparison
        # On deletion: no children -> None; one child -> return it
        # Two children: replace with in-order successor (leftmost of right subtree)
        # Time: O(h), Space: O(h) — find node then replace with in-order successor
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            successor = self._find_min(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root


if __name__ == '__main__':
    sol = Solution()

    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = sol.deleteNode(root, 3)
    vals = tree_to_list(result)
    assert 3 not in vals
    assert 5 in vals and 2 in vals and 4 in vals

    root2 = build_tree([5, 3, 6, 2, 4, None, 7])
    result2 = sol.deleteNode(root2, 0)
    assert tree_to_list(result2) == tree_to_list(build_tree([5, 3, 6, 2, 4, None, 7]))

    assert sol.deleteNode(None, 0) is None

    print("All tests passed.")
