import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // O(n), O(h) — DFS returns int[]{robThis, skipThis}
    public int rob(TreeNode root) {
        int[] res = dfs(root);
        return Math.max(res[0], res[1]);
    }
    private int[] dfs(TreeNode node) {
        if (node == null) return new int[]{0, 0};
        int[] left  = dfs(node.left);
        int[] right = dfs(node.right);
        int robThis  = node.val + left[1] + right[1];
        int skipThis = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{robThis, skipThis};
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
        assert sol.rob(build(new Integer[]{3,2,3,null,3,null,1})) == 7;
        assert sol.rob(build(new Integer[]{3,4,5,1,3,null,1})) == 9;
        assert sol.rob(build(new Integer[]{1})) == 1;
        System.out.println("All tests passed.");
    }
}
