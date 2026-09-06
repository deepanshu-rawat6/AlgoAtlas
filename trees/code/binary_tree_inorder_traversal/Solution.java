import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // Recursive — O(n)
    public List<Integer> inorderRecursive(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res);
        return res;
    }
    private void dfs(TreeNode node, List<Integer> res) {
        if (node == null) return;
        dfs(node.left, res);
        res.add(node.val);
        dfs(node.right, res);
    }

    // Iterative (stack) — O(n)
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) { stack.push(curr); curr = curr.left; }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
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
        assert sol.inorderTraversal(build(new Integer[]{1,null,2,3})).equals(Arrays.asList(1,3,2));
        assert sol.inorderRecursive(build(new Integer[]{1,null,2,3})).equals(Arrays.asList(1,3,2));
        assert sol.inorderTraversal(null).equals(Collections.emptyList());
        assert sol.inorderTraversal(build(new Integer[]{1})).equals(Arrays.asList(1));
        System.out.println("All tests passed.");
    }
}
