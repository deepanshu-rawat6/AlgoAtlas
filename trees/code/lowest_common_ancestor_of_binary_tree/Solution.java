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

    static TreeNode find(TreeNode root, int val) {
        if (root == null) return null;
        if (root.val == val) return root;
        TreeNode l = find(root.left, val);
        return l != null ? l : find(root.right, val);
    }

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left  = lowestCommonAncestor(root.left,  p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }

    public static void main(String[] args) {
        TreeNode root = build(new int[]{3,5,1,6,2,0,8,-1,-1,7,4});

        assert lowestCommonAncestor(root, find(root,5), find(root,1)).val == 3;
        assert lowestCommonAncestor(root, find(root,5), find(root,4)).val == 5;
        assert lowestCommonAncestor(root, find(root,6), find(root,2)).val == 5;

        System.out.println("All tests passed.");
    }
}
