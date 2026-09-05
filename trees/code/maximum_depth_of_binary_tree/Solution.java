// LC 104: Maximum Depth of Binary Tree
// Recursive DFS: 1 + max(left depth, right depth).
// Time: O(n), Space: O(h) recursion stack
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    // Iterative BFS (level count)
    public int maxDepthIter(TreeNode root) {
        if (root == null) return 0;
        int depth = 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            depth++;
            while (sz-- > 0) {
                TreeNode n = q.poll();
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
        }
        return depth;
    }

    // Optimal recursive DFS: O(n)
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    static TreeNode build(int[] vals) {
        if (vals.length == 0 || vals[0] == -1) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>(); q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (i < vals.length && vals[i] != -1) { node.left = new TreeNode(vals[i]); q.add(node.left); } i++;
            if (i < vals.length && vals[i] != -1) { node.right = new TreeNode(vals[i]); q.add(node.right); } i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.maxDepth(build(new int[]{3,9,20,-1,-1,15,7})) == 3 : "Test 1 failed";
        assert s.maxDepth(build(new int[]{1,-1,2})) == 2 : "Test 2 failed";
        assert s.maxDepth(null) == 0 : "Test 3 failed";
        assert s.maxDepth(build(new int[]{1})) == 1 : "Test 4 failed";
        assert s.maxDepth(build(new int[]{1,2,3,4,5})) == 3 : "Test 5 failed";
        System.out.println("All tests passed.");
    }
}
