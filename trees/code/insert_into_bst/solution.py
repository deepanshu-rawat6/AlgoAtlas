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
    ## 701. Insert into a Binary Search Tree

    You are given the `root` node of a BST and a `val` to insert into the tree.
    Return the root node of the BST after the insertion. It is guaranteed that the new value
    does not exist in the original BST.

    There may exist multiple valid ways for the insertion, as long as the tree remains a BST
    after insertion. You can return any of them.

    ### Examples

    ```text
    Example 1:
    Input:  root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]

    Example 2:
    Input:  root = [40,20,60,10,30,50,70], val = 25
    Output: [40,20,60,10,30,50,70,null,null,25]

    Example 3:
    Input:  root = [], val = 5
    Output: [5]
    ```

    ### Constraints
    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-10^8 <= Node.val <= 10^8`
    - All the values `Node.val` are unique.
    - `-10^8 <= val <= 10^8`
    - It's guaranteed that `val` does not exist in the original BST.
    """

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Navigate left if val < root.val, right if val > root.val
        # Insert at the first None position found
        # Time: O(h), Space: O(h) — recurse to the correct leaf position
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Time: O(h), Space: O(1) — walk to insertion point without recursion
        new_node = TreeNode(val)
        if not root:
            return new_node
        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = new_node
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = new_node
                    break
                cur = cur.right
        return root


if __name__ == '__main__':
    sol = Solution()

    root = build_tree([4, 2, 7, 1, 3])
    result = sol.insertIntoBST(root, 5)
    assert 5 in tree_to_list(result)

    root2 = build_tree([4, 2, 7, 1, 3])
    result2 = sol.insertIntoBST_iterative(root2, 5)
    assert 5 in tree_to_list(result2)

    assert sol.insertIntoBST(None, 5).val == 5

    print("All tests passed.")
