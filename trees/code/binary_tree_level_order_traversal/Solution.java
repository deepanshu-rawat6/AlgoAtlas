// LC 102: Binary Tree Level Order Traversal
// BFS with a queue, collect each level into a separate list.
// Time: O(n), Space: O(n)
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            while (sz-- > 0) {
                TreeNode n = q.poll();
                level.add(n.val);
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
            res.add(level);
        }
        return res;
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
        assert s.levelOrder(build(new int[]{3,9,20,-1,-1,15,7})).equals(
            Arrays.asList(Arrays.asList(3), Arrays.asList(9,20), Arrays.asList(15,7))) : "Test 1 failed";
        assert s.levelOrder(build(new int[]{1})).equals(
            Arrays.asList(Arrays.asList(1))) : "Test 2 failed";
        assert s.levelOrder(null).isEmpty() : "Test 3 failed";
        assert s.levelOrder(build(new int[]{1,2,3,4,5})).equals(
            Arrays.asList(Arrays.asList(1), Arrays.asList(2,3), Arrays.asList(4,5))) : "Test 4 failed";
        System.out.println("All tests passed.");
    }
}
