import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // O(n) — DFS returning height; update diameter at each node
    public int diameterOfBinaryTree(TreeNode root) {
        int[] diameter = {0};
        depth(root, diameter);
        return diameter[0];
    }
    private int depth(TreeNode node, int[] diameter) {
        if (node == null) return 0;
        int left  = depth(node.left,  diameter);
        int right = depth(node.right, diameter);
        diameter[0] = Math.max(diameter[0], left + right);
        return 1 + Math.max(left, right);
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
        assert sol.diameterOfBinaryTree(build(new Integer[]{1,2,3,4,5})) == 3;
        assert sol.diameterOfBinaryTree(build(new Integer[]{1,2})) == 1;
        assert sol.diameterOfBinaryTree(build(new Integer[]{1})) == 0;
        System.out.println("All tests passed.");
    }
}
