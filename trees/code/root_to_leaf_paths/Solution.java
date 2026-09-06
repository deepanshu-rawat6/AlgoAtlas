import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    private void dfs(TreeNode node, String path, List<String> res) {
        if (node.left == null && node.right == null) { res.add(path); return; }
        if (node.left  != null) dfs(node.left,  path + "->" + node.left.val,  res);
        if (node.right != null) dfs(node.right, path + "->" + node.right.val, res);
    }

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root != null) dfs(root, String.valueOf(root.val), res);
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r1 = new TreeNode(1);
        r1.left = new TreeNode(2); r1.right = new TreeNode(3);
        r1.left.right = new TreeNode(5);
        List<String> p1 = sol.binaryTreePaths(r1);
        Collections.sort(p1);
        assert p1.equals(Arrays.asList("1->2->5","1->3")) : "test1 failed: " + p1;

        List<String> p2 = sol.binaryTreePaths(new TreeNode(1));
        assert p2.equals(Arrays.asList("1")) : "test2 failed";

        TreeNode r3 = new TreeNode(1);
        r3.left = new TreeNode(2);
        assert sol.binaryTreePaths(r3).equals(Arrays.asList("1->2")) : "test3 failed";

        System.out.println("All tests passed.");
    }
}
