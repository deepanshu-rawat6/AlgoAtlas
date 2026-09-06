import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // Approach 1: reverse postorder (right→left→root) — O(n), O(h) space
    public void flatten(TreeNode root) {
        TreeNode[] prev = {null};
        dfs(root, prev);
    }
    private void dfs(TreeNode node, TreeNode[] prev) {
        if (node == null) return;
        dfs(node.right, prev);
        dfs(node.left,  prev);
        node.right = prev[0];
        node.left  = null;
        prev[0]    = node;
    }

    // Approach 2: Morris-like iterative — O(n), O(1) space
    public void flattenIterative(TreeNode root) {
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left != null) {
                TreeNode rightmost = curr.left;
                while (rightmost.right != null) rightmost = rightmost.right;
                rightmost.right = curr.right;
                curr.right = curr.left;
                curr.left  = null;
            }
            curr = curr.right;
        }
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

    static List<Integer> toList(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        while (root != null) {
            assert root.left == null : "left not null at " + root.val;
            res.add(root.val);
            root = root.right;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r1 = build(new Integer[]{1,2,5,3,4,null,6});
        sol.flatten(r1);
        assert toList(r1).equals(Arrays.asList(1,2,3,4,5,6));

        TreeNode r2 = build(new Integer[]{1,2,5,3,4,null,6});
        sol.flattenIterative(r2);
        assert toList(r2).equals(Arrays.asList(1,2,3,4,5,6));

        TreeNode r3 = build(new Integer[]{1});
        sol.flatten(r3);
        assert toList(r3).equals(Arrays.asList(1));

        System.out.println("All tests passed.");
    }
}
