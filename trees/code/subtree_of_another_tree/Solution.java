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

    static boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null || s.val != t.val) return false;
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }

    static boolean isSubtree(TreeNode root, TreeNode sub) {
        if (root == null) return false;
        if (isSame(root, sub)) return true;
        return isSubtree(root.left, sub) || isSubtree(root.right, sub);
    }

    public static void main(String[] args) {
        assert isSubtree(build(new int[]{3,4,5,1,2}), build(new int[]{4,1,2}));
        assert !isSubtree(build(new int[]{3,4,5,1,2,-1,-1,-1,-1,0}), build(new int[]{4,1,2}));
        assert !isSubtree(null, build(new int[]{1}));
        System.out.println("All tests passed.");
    }
}
