import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // Approach 1: simple DFS — O(n)
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }

    // Approach 2: O(log^2 n) — compare left-height vs right-height
    public int countNodesFast(TreeNode root) {
        if (root == null) return 0;
        int lh = 0, rh = 0;
        TreeNode l = root, r = root;
        while (l != null) { lh++; l = l.left; }
        while (r != null) { rh++; r = r.right; }
        if (lh == rh) return (1 << lh) - 1;
        return 1 + countNodesFast(root.left) + countNodesFast(root.right);
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

    public static void main(String[] args) {
        Solution sol = new Solution();
        TreeNode t1 = build(new Integer[]{1,2,3,4,5,6});
        assert sol.countNodes(t1) == 6;
        assert sol.countNodesFast(build(new Integer[]{1,2,3,4,5,6})) == 6;
        assert sol.countNodesFast(null) == 0;
        assert sol.countNodesFast(build(new Integer[]{1})) == 1;
        System.out.println("All tests passed.");
    }
}
