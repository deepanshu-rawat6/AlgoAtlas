import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode build(int[] v) {
        if (v == null || v.length == 0 || v[0] == -1) return null;
        TreeNode root = new TreeNode(v[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < v.length) {
            TreeNode n = q.poll();
            if (i < v.length && v[i] != -1) { n.left  = new TreeNode(v[i]); q.add(n.left);  } i++;
            if (i < v.length && v[i] != -1) { n.right = new TreeNode(v[i]); q.add(n.right); } i++;
        }
        return root;
    }

    static boolean isMirror(TreeNode l, TreeNode r) {
        if (l == null && r == null) return true;
        if (l == null || r == null || l.val != r.val) return false;
        return isMirror(l.left, r.right) && isMirror(l.right, r.left);
    }

    static boolean isSymmetric(TreeNode root) {
        return root != null && isMirror(root.left, root.right);
    }

    public static void main(String[] args) {
        assert isSymmetric(build(new int[]{1,2,2,3,4,4,3}));
        assert !isSymmetric(build(new int[]{1,2,2,-1,3,-1,3}));
        assert isSymmetric(build(new int[]{1}));
        System.out.println("All tests passed.");
    }
}
