import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    private TreeNode first, second, prev;

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev != null && prev.val > node.val) {
            second = node;
            if (first == null) first = prev;
        }
        prev = node;
        inorder(node.right);
    }

    public void recoverTree(TreeNode root) {
        first = second = prev = null;
        inorder(root);
        if (first != null && second != null) {
            int tmp = first.val; first.val = second.val; second.val = tmp;
        }
    }

    private List<Integer> toInorder(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) { stack.push(cur); cur = cur.left; }
            cur = stack.pop();
            res.add(cur.val);
            cur = cur.right;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // [1,3,null,null,2] -> [1,2,3]
        TreeNode r1 = new TreeNode(1);
        r1.left = new TreeNode(3); r1.left.right = new TreeNode(2);
        sol.recoverTree(r1);
        assert sol.toInorder(r1).equals(Arrays.asList(1,2,3)) : "test1 failed";

        // [3,1,4,null,null,2] -> [1,2,3,4]
        TreeNode r2 = new TreeNode(3);
        r2.left = new TreeNode(1); r2.right = new TreeNode(4);
        r2.right.left = new TreeNode(2);
        sol.recoverTree(r2);
        assert sol.toInorder(r2).equals(Arrays.asList(1,2,3,4)) : "test2 failed";

        // [2,3,1] -> [1,2,3]
        TreeNode r3 = new TreeNode(2);
        r3.left = new TreeNode(3); r3.right = new TreeNode(1);
        sol.recoverTree(r3);
        assert sol.toInorder(r3).equals(Arrays.asList(1,2,3)) : "test3 failed";

        System.out.println("All tests passed.");
    }
}
