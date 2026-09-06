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

    static TreeNode inorderSuccessor(TreeNode root, int pval) {
        TreeNode succ = null;
        while (root != null) {
            if (pval < root.val) { succ = root; root = root.left; }
            else                 { root = root.right; }
        }
        return succ;
    }

    static TreeNode inorderPredecessor(TreeNode root, int pval) {
        TreeNode pred = null;
        while (root != null) {
            if (pval > root.val) { pred = root; root = root.right; }
            else                 { root = root.left; }
        }
        return pred;
    }

    public static void main(String[] args) {
        TreeNode root = build(new int[]{5,3,6,2,4,-1,-1,1});

        assert inorderSuccessor(root, 3).val == 4;
        assert inorderPredecessor(root, 3).val == 2;

        assert inorderSuccessor(root, 6) == null;
        assert inorderPredecessor(root, 1) == null;

        assert inorderSuccessor(root, 5).val == 6;
        assert inorderPredecessor(root, 5).val == 4;

        System.out.println("All tests passed.");
    }
}
