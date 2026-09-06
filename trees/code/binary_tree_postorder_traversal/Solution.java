import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // Recursive — O(n)
    public List<Integer> postorderRecursive(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res);
        return res;
    }
    private void dfs(TreeNode node, List<Integer> res) {
        if (node == null) return;
        dfs(node.left, res);
        dfs(node.right, res);
        res.add(node.val);
    }

    // Iterative: push to stack, collect reversed — O(n)
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            res.add(node.val);
            if (node.left  != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        Collections.reverse(res);
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
        assert sol.postorderTraversal(build(new Integer[]{1,null,2,3})).equals(Arrays.asList(3,2,1));
        assert sol.postorderRecursive(build(new Integer[]{1,null,2,3})).equals(Arrays.asList(3,2,1));
        assert sol.postorderTraversal(null).equals(Collections.emptyList());
        assert sol.postorderTraversal(build(new Integer[]{1})).equals(Arrays.asList(1));
        System.out.println("All tests passed.");
    }
}
