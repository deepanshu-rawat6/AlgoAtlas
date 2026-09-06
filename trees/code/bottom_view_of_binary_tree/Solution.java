import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // BFS with column; overwrite per column → last seen = bottom view — O(n)
    public List<Integer> bottomView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        TreeMap<Integer, Integer> colMap = new TreeMap<>();
        Queue<int[]> queue = new LinkedList<>();   // [node encoded as index + col]
        // Use a node+col pair via a wrapper
        Queue<Object[]> q = new LinkedList<>();
        q.add(new Object[]{root, 0});
        while (!q.isEmpty()) {
            Object[] pair = q.poll();
            TreeNode node = (TreeNode) pair[0];
            int col = (int) pair[1];
            colMap.put(col, node.val);
            if (node.left  != null) q.add(new Object[]{node.left,  col - 1});
            if (node.right != null) q.add(new Object[]{node.right, col + 1});
        }
        res.addAll(colMap.values());
        return res;
    }

    static TreeNode build(Integer[] vals) {
        if (vals == null || vals.length == 0 || vals[0] == null) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (i < vals.length && vals[i] != null) { node.left = new TreeNode(vals[i]); q.add(node.left); }
            i++;
            if (i < vals.length && vals[i] != null) { node.right = new TreeNode(vals[i]); q.add(node.right); }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.bottomView(build(new Integer[]{1,2,3,4,5,6,7})).equals(Arrays.asList(4,2,6,3,7));
        assert sol.bottomView(build(new Integer[]{1,2,3})).equals(Arrays.asList(2,1,3));
        assert sol.bottomView(build(new Integer[]{5})).equals(Arrays.asList(5));
        System.out.println("All tests passed.");
    }
}
