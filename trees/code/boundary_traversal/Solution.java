import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // root + left boundary (excl leaves) + all leaves + right boundary reversed (excl leaves) — O(n)
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        res.add(root.val);
        if (!isLeaf(root)) {
            addLeftBoundary(root.left, res);
            addLeaves(root.left, res);
            addLeaves(root.right, res);
            addRightBoundary(root.right, res);
        }
        return res;
    }

    private boolean isLeaf(TreeNode n) { return n != null && n.left == null && n.right == null; }

    private void addLeftBoundary(TreeNode node, List<Integer> res) {
        while (node != null) {
            if (!isLeaf(node)) res.add(node.val);
            node = node.left != null ? node.left : node.right;
        }
    }

    private void addLeaves(TreeNode node, List<Integer> res) {
        if (node == null) return;
        if (isLeaf(node)) { res.add(node.val); return; }
        addLeaves(node.left, res);
        addLeaves(node.right, res);
    }

    private void addRightBoundary(TreeNode node, List<Integer> res) {
        List<Integer> tmp = new ArrayList<>();
        while (node != null) {
            if (!isLeaf(node)) tmp.add(node.val);
            node = node.right != null ? node.right : node.left;
        }
        Collections.reverse(tmp);
        res.addAll(tmp);
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
        assert sol.boundaryOfBinaryTree(build(new Integer[]{1,2,3,4,5,6,7})).equals(Arrays.asList(1,2,4,5,6,7,3));
        assert sol.boundaryOfBinaryTree(build(new Integer[]{1})).equals(Arrays.asList(1));
        // [1,2,null,3]: left boundary=2, leaf=3, no right boundary
        assert sol.boundaryOfBinaryTree(build(new Integer[]{1,2,null,3})).equals(Arrays.asList(1,2,3));
        System.out.println("All tests passed.");
    }
}
