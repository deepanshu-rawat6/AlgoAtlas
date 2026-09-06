import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // O(n) — DFS tracking max value seen on path from root
    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }
    private int dfs(TreeNode node, int maxSoFar) {
        if (node == null) return 0;
        int count = node.val >= maxSoFar ? 1 : 0;
        int newMax = Math.max(maxSoFar, node.val);
        return count + dfs(node.left, newMax) + dfs(node.right, newMax);
    }

    static TreeNode build(Integer[] vals) {
        if (vals == null || vals.length == 0) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (i < vals.length && vals[i] != null) { node.left  = new TreeNode(vals[i]); q.add(node.left);  } i++;
            if (i < vals.length && vals[i] != null) { node.right = new TreeNode(vals[i]); q.add(node.right); } i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.goodNodes(build(new Integer[]{3,1,4,3,null,1,5})) == 4;
        assert sol.goodNodes(build(new Integer[]{3,3,null,4,2})) == 3;
        assert sol.goodNodes(build(new Integer[]{1})) == 1;
        System.out.println("All tests passed.");
    }
}
