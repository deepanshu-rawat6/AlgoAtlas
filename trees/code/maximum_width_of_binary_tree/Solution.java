import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        int maxW = 0;
        // Queue of long[] {nodeRef-via-index trick: we'll use a wrapper}
        // Use Deque<long[]> where [0]=nodeId (can't store node ref alongside long easily)
        // Instead use two parallel queues
        Queue<TreeNode> nodes = new LinkedList<>();
        Queue<Long> indices = new LinkedList<>();
        nodes.add(root);
        indices.add(0L);
        while (!nodes.isEmpty()) {
            int sz = nodes.size();
            long first = indices.peek();
            long last = first;
            for (int i = 0; i < sz; i++) {
                TreeNode node = nodes.poll();
                long idx = indices.poll() - first; // normalize
                last = idx;
                if (node.left  != null) { nodes.add(node.left);  indices.add(2 * idx); }
                if (node.right != null) { nodes.add(node.right); indices.add(2 * idx + 1); }
            }
            maxW = (int) Math.max(maxW, last + 1);
        }
        return maxW;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // [1,3,2,5,3,null,9] -> 4
        TreeNode r1 = new TreeNode(1);
        r1.left = new TreeNode(3); r1.right = new TreeNode(2);
        r1.left.left = new TreeNode(5); r1.left.right = new TreeNode(3);
        r1.right.right = new TreeNode(9);
        assert sol.widthOfBinaryTree(r1) == 4 : "expected 4";

        // single node -> 1
        assert sol.widthOfBinaryTree(new TreeNode(1)) == 1 : "expected 1";

        // null -> 0
        assert sol.widthOfBinaryTree(null) == 0 : "expected 0";

        // deep asymmetric -> 7
        TreeNode r3 = new TreeNode(1);
        r3.left = new TreeNode(3); r3.right = new TreeNode(2);
        r3.left.left = new TreeNode(5);
        r3.right.right = new TreeNode(9);
        r3.left.left.left = new TreeNode(6);
        r3.right.right.left = new TreeNode(7);
        assert sol.widthOfBinaryTree(r3) == 7 : "expected 7";

        System.out.println("All tests passed.");
    }
}
