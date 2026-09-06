import java.util.LinkedList;
import java.util.Queue;
import java.util.Deque;
import java.util.ArrayDeque;

class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode build(int[] vals) {
        if (vals == null || vals.length == 0 || vals[0] == -1) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (vals[i] != -1) { node.left = new TreeNode(vals[i]); q.add(node.left); }
            i++;
            if (i < vals.length && vals[i] != -1) { node.right = new TreeNode(vals[i]); q.add(node.right); }
            i++;
        }
        return root;
    }

    static int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        int count = 0;
        while (root != null || !stack.isEmpty()) {
            while (root != null) { stack.push(root); root = root.left; }
            root = stack.pop();
            if (++count == k) return root.val;
            root = root.right;
        }
        return -1;
    }

    public static void main(String[] args) {
        assert kthSmallest(build(new int[]{3,1,4,-1,2}), 1) == 1;
        assert kthSmallest(build(new int[]{5,3,6,2,4,-1,-1,1}), 3) == 3;
        assert kthSmallest(build(new int[]{5,3,6,2,4,-1,-1,1}), 1) == 1;
        System.out.println("All tests passed.");
    }
}
