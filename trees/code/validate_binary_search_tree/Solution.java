import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    static TreeNode build(int[] v) {
        if (v == null || v.length == 0 || v[0] == -1) return null;
        TreeNode root = new TreeNode(v[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < v.length) {
            TreeNode node = q.poll();
            if (i < v.length && v[i] != -1) { node.left  = new TreeNode(v[i]); q.add(node.left); }  i++;
            if (i < v.length && v[i] != -1) { node.right = new TreeNode(v[i]); q.add(node.right); } i++;
        }
        return root;
    }

    static boolean validate(TreeNode node, long lo, long hi) {
        if (node == null) return true;
        if (node.val <= lo || node.val >= hi) return false;
        return validate(node.left, lo, node.val) && validate(node.right, node.val, hi);
    }

    static boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public static void main(String[] args) {
        assert isValidBST(build(new int[]{2,1,3}))             == true;
        assert isValidBST(build(new int[]{5,1,4,-1,-1,3,6}))  == false;
        assert isValidBST(build(new int[]{2,2,2}))             == false;
        System.out.println("All tests passed.");
    }
}
