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

    static TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (root.val == val) return root;
            root = (val < root.val) ? root.left : root.right;
        }
        return null;
    }

    public static void main(String[] args) {
        TreeNode root = build(new int[]{4, 2, 7, 1, 3});
        assert searchBST(root, 2) != null && searchBST(root, 2).val == 2;
        assert searchBST(root, 5) == null;
        assert searchBST(root, 4) == root;
        System.out.println("All tests passed.");
    }
}
