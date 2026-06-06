"""
Tree Traversals
===============
Covers all standard binary tree traversal strategies.

Traversals:
  - Inorder   (Left → Root → Right): gives sorted order for BST
  - Preorder  (Root → Left → Right): used for tree serialization/copying
  - Postorder (Left → Right → Root): used for deletion, expression evaluation
  - Level-order (BFS): shortest path, level-by-level processing
  - Morris Traversal: O(1) space inorder/preorder using threaded tree

Time Complexity:  O(n) for all traversals
Space Complexity: O(h) recursive/iterative (h = tree height), O(1) Morris
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Recursive ────────────────────────────────────────────────────────────────

def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result


# ─── Iterative ────────────────────────────────────────────────────────────────

def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Use explicit stack; go left as far as possible, then process, then right."""
    result, stack, curr = [], [], root
    while curr or stack:
        while curr:              # push all left nodes
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()       # process node
        result.append(curr.val)
        curr = curr.right        # move to right subtree
    return result


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Process node on push; push right before left so left is processed first."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Reverse of modified preorder (Root→Right→Left) gives Left→Right→Root."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


# ─── Level-order (BFS) ────────────────────────────────────────────────────────

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """BFS using a deque; snapshot queue size at start of each level."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):   # process exactly one level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# ─── Morris Traversal (O(1) space) ────────────────────────────────────────────

def morris_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Threads the tree: for each node, find inorder predecessor and point its
    right child to current node. Unthread when revisiting.

    No stack/recursion — O(1) extra space.
    """
    result, curr = [], root
    while curr:
        if not curr.left:
            result.append(curr.val)   # no left subtree, process and go right
            curr = curr.right
        else:
            # find inorder predecessor (rightmost node in left subtree)
            pred = curr.left
            while pred.right and pred.right is not curr:
                pred = pred.right

            if not pred.right:
                pred.right = curr     # create thread
                curr = curr.left
            else:
                pred.right = None     # remove thread
                result.append(curr.val)
                curr = curr.right
    return result


def morris_preorder(root: Optional[TreeNode]) -> List[int]:
    """Same threading trick; collect node value when creating thread (not removing)."""
    result, curr = [], root
    while curr:
        if not curr.left:
            result.append(curr.val)
            curr = curr.right
        else:
            pred = curr.left
            while pred.right and pred.right is not curr:
                pred = pred.right

            if not pred.right:
                result.append(curr.val)  # collect here (before going left)
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                curr = curr.right
    return result


# ─── Helpers ──────────────────────────────────────────────────────────────────

def build_tree(values: List) -> Optional[TreeNode]:
    """Build tree from level-order list (None = missing node)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = build_tree([4, 2, 6, 1, 3, 5, 7])

    print("Inorder   recursive:", inorder_recursive(root))    # [1,2,3,4,5,6,7]
    print("Inorder   iterative:", inorder_iterative(root))
    print("Inorder   Morris:   ", morris_inorder(root))

    print("Preorder  recursive:", preorder_recursive(root))   # [4,2,1,3,6,5,7]
    print("Preorder  iterative:", preorder_iterative(root))
    print("Preorder  Morris:   ", morris_preorder(root))

    print("Postorder recursive:", postorder_recursive(root))  # [1,3,2,5,7,6,4]
    print("Postorder iterative:", postorder_iterative(root))

    print("Level-order:        ", level_order(root))          # [[4],[2,6],[1,3,5,7]]
