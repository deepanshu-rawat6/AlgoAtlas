import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // DFS: at each node, max path through it = val + max(0,left) + max(0,right) — O(n)
    public int maxPathSum(TreeNode root) {
        int[] maxSum = {Integer.MIN_VALUE};
        dfs(root, maxSum);
        return maxSum[0];
    }

    private int dfs(TreeNode node, int[] maxSum) {
        if (node == null) return 0;
        int left  = Math.max(0, dfs(node.left,  maxSum));
        int right = Math.max(0, dfs(node.right, maxSum));
        maxSum[0] = Math.max(maxSum[0], node.val + left + right);
        return node.val + Math.max(left, right);
    }

    static TreeNode build(Integer[] vals) {
        if (vals == null || vals.length == 0 || vals[0] == null) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (i < vals.length && vals[i] != null) { node.left = new TreeNode(vals[i]); q.add(node.left); }
            i++;
            if (i < vals.length && vals[i] != null) { node.right = new TreeNode(vals[i]); q.add(node.right); }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxPathSum(build(new Integer[]{1,2,3})) == 6;
        assert sol.maxPathSum(build(new Integer[]{-10,9,20,null,null,15,7})) == 42;
        assert sol.maxPathSum(build(new Integer[]{-3})) == -3;
        System.out.println("All tests passed.");
    }
}
