import java.util.ArrayDeque;
import java.util.Queue;

class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode build(int[] v) {
        if (v == null || v.length == 0 || v[0] == -1) return null;
        TreeNode root = new TreeNode(v[0]);
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < v.length) {
            TreeNode n = q.poll();
            if (i < v.length && v[i] != -1) { n.left  = new TreeNode(v[i]); q.add(n.left);  } i++;
            if (i < v.length && v[i] != -1) { n.right = new TreeNode(v[i]); q.add(n.right); } i++;
        }
        return root;
    }

    static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public static void main(String[] args) {
        assert isSameTree(build(new int[]{1,2,3}), build(new int[]{1,2,3}));
        assert !isSameTree(build(new int[]{1,2,-1}), build(new int[]{1,-1,2}));
        assert !isSameTree(build(new int[]{1,2,1}), build(new int[]{1,1,2}));
        assert isSameTree(null, null);
        System.out.println("All tests passed.");
    }
}
