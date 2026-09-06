import java.util.LinkedList;
import java.util.Queue;

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

    static boolean contains(TreeNode root, int val) {
        while (root != null) {
            if (root.val == val) return true;
            root = (val < root.val) ? root.left : root.right;
        }
        return false;
    }

    static TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left  = insertIntoBST(root.left,  val);
        else                root.right = insertIntoBST(root.right, val);
        return root;
    }

    public static void main(String[] args) {
        TreeNode r1 = build(new int[]{4,2,7,1,3});
        insertIntoBST(r1, 5);
        assert contains(r1, 5);

        assert insertIntoBST(null, 42).val == 42;

        TreeNode r2 = build(new int[]{40,20,60,10,30,50,70});
        insertIntoBST(r2, 25);
        assert contains(r2, 25);

        System.out.println("All tests passed.");
    }
}
