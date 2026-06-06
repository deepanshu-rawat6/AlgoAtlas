"""
LC 103 - Binary Tree Zigzag Level Order Traversal

Problem: Return the zigzag level order traversal of a binary tree's values
(i.e., from left to right, then right to left for the next level, alternating).

Example:
    Input:  [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

Constraints:
    - Number of nodes: [0, 2000]
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
    if not vals: return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach: BFS with direction flag — O(n) time, O(n) space
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            # reverse odd levels (right-to-left direction)
            result.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return result
    
    # Using deque in level to simplify and not change the BFS logic
    def zigzagLevelOrderDeque(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []

            # Use left_to_right for clearer state tracking. Root level is left-to-right.
            left_to_right = True 
            res, queue = [], deque([root])
            
            while queue:
                level = deque() # Use a deque for the level's values
                
                for _ in range(len(queue)):
                    # ALWAYS process the main queue in standard BFS order
                    node = queue.popleft()
                    
                    # Determine where to place the value in our level list
                    if left_to_right:
                        level.append(node.val)
                    else:
                        level.appendleft(node.val)
                    
                    # ALWAYS append children in standard order (left then right)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                # Toggle the direction for the next level
                left_to_right = not left_to_right
                res.append(list(level))
            
            return res


if __name__ == "__main__":
    sol = Solution()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert sol.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

    assert sol.zigzagLevelOrder(None) == []

    root2 = build_tree([1])
    assert sol.zigzagLevelOrder(root2) == [[1]]

    print("All tests passed.")
