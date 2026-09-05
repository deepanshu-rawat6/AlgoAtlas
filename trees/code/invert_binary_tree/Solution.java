// LC 226: Invert Binary Tree
// Swap left and right children recursively.
// Time: O(n), Space: O(h) recursion stack
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    // Iterative BFS
    public TreeNode invertTreeIter(TreeNode root) {
        if (root == null) return null;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            TreeNode tmp = node.left; node.left = node.right; node.right = tmp;
            if (node.left != null) q.add(node.left);
            if (node.right != null) q.add(node.right);
        }
        return root;
    }

    // Optimal recursive DFS: O(n)
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode tmp = root.left; root.left = root.right; root.right = tmp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }

    static TreeNode build(int[] vals) {
        if (vals.length == 0 || vals[0] == -1) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (i < vals.length && vals[i] != -1) { node.left = new TreeNode(vals[i]); q.add(node.left); }
            i++;
            if (i < vals.length && vals[i] != -1) { node.right = new TreeNode(vals[i]); q.add(node.right); }
            i++;
        }
        return root;
    }

    static List<Integer> levelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            res.add(n.val);
            if (n.left != null) q.add(n.left);
            if (n.right != null) q.add(n.right);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert levelOrder(s.invertTree(build(new int[]{4,2,7,1,3,6,9}))).equals(Arrays.asList(4,7,2,9,6,3,1)) : "Test 1 failed";
        assert levelOrder(s.invertTree(build(new int[]{2,1,3}))).equals(Arrays.asList(2,3,1)) : "Test 2 failed";
        assert s.invertTree(null) == null : "Test 3 failed";
        assert levelOrder(s.invertTree(build(new int[]{1}))).equals(Arrays.asList(1)) : "Test 4 failed";
        System.out.println("All tests passed.");
    }
}
