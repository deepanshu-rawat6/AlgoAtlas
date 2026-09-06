import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // O(n) — postorder: process children first, then delete if became leaf with target val
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root == null) return null;
        root.left  = removeLeafNodes(root.left,  target);
        root.right = removeLeafNodes(root.right, target);
        if (root.left == null && root.right == null && root.val == target) return null;
        return root;
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

    static List<Integer> bfsList(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n != null) { res.add(n.val); q.add(n.left); q.add(n.right); }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r1 = build(new Integer[]{1,2,3,2,null,2,4});
        List<Integer> res1 = bfsList(sol.removeLeafNodes(r1, 2));
        assert !res1.contains(2) : "Expected no 2s, got " + res1;

        assert sol.removeLeafNodes(build(new Integer[]{1}), 1) == null;

        TreeNode r3 = build(new Integer[]{1,2,null,2,null,2});
        TreeNode res3 = sol.removeLeafNodes(r3, 2);
        assert res3 != null && res3.val == 1 && res3.left == null && res3.right == null;

        System.out.println("All tests passed.");
    }
}
