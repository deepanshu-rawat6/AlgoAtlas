import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode build(int[] vals) {
        if (vals == null || vals.length == 0 || vals[0] == -1) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (vals[i] != -1) { node.left = new TreeNode(vals[i]); q.add(node.left); }
            i++;
            if (i < vals.length && vals[i] != -1) { node.right = new TreeNode(vals[i]); q.add(node.right); }
            i++;
        }
        return root;
    }

    static int maxSize;

    // Returns int[]{isBST(1/0), size, min, max}
    static int[] dfs(TreeNode node) {
        if (node == null) return new int[]{1, 0, Integer.MAX_VALUE, Integer.MIN_VALUE};
        int[] l = dfs(node.left);
        int[] r = dfs(node.right);
        if (l[0] == 1 && r[0] == 1 && l[3] < node.val && node.val < r[2]) {
            int size = l[1] + r[1] + 1;
            maxSize = Math.max(maxSize, size);
            return new int[]{1, size, Math.min(l[2], node.val), Math.max(r[3], node.val)};
        }
        return new int[]{0, 0, 0, 0};
    }

    static int largestBSTSubtree(TreeNode root) {
        maxSize = 0;
        dfs(root);
        return maxSize;
    }

    public static void main(String[] args) {
        assert largestBSTSubtree(build(new int[]{10,5,15,1,8,-1,7})) == 3;
        assert largestBSTSubtree(build(new int[]{4,2,6,1,3,5,7})) == 7;
        assert largestBSTSubtree(build(new int[]{1})) == 1;
        System.out.println("All tests passed.");
    }
}
