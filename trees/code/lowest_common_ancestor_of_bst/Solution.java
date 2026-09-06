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

    static TreeNode findNode(TreeNode root, int val) {
        while (root != null) {
            if (root.val == val) return root;
            root = (val < root.val) ? root.left : root.right;
        }
        return null;
    }

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (p.val < root.val && q.val < root.val) root = root.left;
            else if (p.val > root.val && q.val > root.val) root = root.right;
            else return root;
        }
        return null;
    }

    public static void main(String[] args) {
        TreeNode root = build(new int[]{6,2,8,0,4,7,9,-1,-1,3,5});

        assert lowestCommonAncestor(root, findNode(root,2), findNode(root,8)).val == 6;
        assert lowestCommonAncestor(root, findNode(root,2), findNode(root,4)).val == 2;
        assert lowestCommonAncestor(root, findNode(root,0), findNode(root,5)).val == 2;

        System.out.println("All tests passed.");
    }
}
