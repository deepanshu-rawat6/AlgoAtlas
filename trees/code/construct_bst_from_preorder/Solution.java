import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // Approach 1: recursive with upper bound — O(n)
    public TreeNode bstFromPreorderRecursive(int[] preorder) {
        int[] idx = {0};
        return build(preorder, idx, Double.MAX_VALUE);
    }
    private TreeNode build(int[] pre, int[] idx, double upper) {
        if (idx[0] == pre.length || pre[idx[0]] > upper) return null;
        int val = pre[idx[0]++];
        TreeNode node = new TreeNode(val);
        node.left  = build(pre, idx, val);
        node.right = build(pre, idx, upper);
        return node;
    }

    // Approach 2: stack-based — O(n)
    public TreeNode bstFromPreorder(int[] preorder) {
        if (preorder.length == 0) return null;
        TreeNode root = new TreeNode(preorder[0]);
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        for (int i = 1; i < preorder.length; i++) {
            TreeNode node = new TreeNode(preorder[i]);
            if (preorder[i] < stack.peek().val) {
                stack.peek().left = node;
            } else {
                TreeNode parent = stack.peek();
                while (!stack.isEmpty() && stack.peek().val < preorder[i])
                    parent = stack.pop();
                parent.right = node;
            }
            stack.push(node);
        }
        return root;
    }

    static List<Integer> inorder(TreeNode node) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = node;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop(); res.add(cur.val); cur = cur.right;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] pre1 = {8,5,1,7,10,12};
        assert sol.inorder(sol.bstFromPreorder(pre1)).equals(Arrays.asList(1,5,7,8,10,12));
        assert sol.inorder(sol.bstFromPreorderRecursive(pre1)).equals(Arrays.asList(1,5,7,8,10,12));

        TreeNode t = sol.bstFromPreorder(new int[]{1});
        assert t.val == 1 && t.left == null && t.right == null;

        assert sol.inorder(sol.bstFromPreorder(new int[]{4,3,2,1})).equals(Arrays.asList(1,2,3,4));
        System.out.println("All tests passed.");
    }
}
