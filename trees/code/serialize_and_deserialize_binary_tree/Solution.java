import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static String serialize(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (sb.length() > 0) sb.append(',');
            if (n == null) { sb.append("null"); continue; }
            sb.append(n.val);
            q.add(n.left);
            q.add(n.right);
        }
        return sb.toString();
    }

    static TreeNode deserialize(String data) {
        if (data == null || data.isEmpty()) return null;
        String[] tokens = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(tokens[0]));
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tokens.length) {
            TreeNode n = q.poll();
            if (!tokens[i].equals("null")) { n.left  = new TreeNode(Integer.parseInt(tokens[i])); q.add(n.left);  } i++;
            if (i < tokens.length && !tokens[i].equals("null")) { n.right = new TreeNode(Integer.parseInt(tokens[i])); q.add(n.right); } i++;
        }
        return root;
    }

    static List<Integer> inorder(TreeNode n) {
        List<Integer> out = new ArrayList<>();
        inorderHelper(n, out);
        return out;
    }
    static void inorderHelper(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorderHelper(n.left, out);
        out.add(n.val);
        inorderHelper(n.right, out);
    }

    static TreeNode build(int[] v) {
        if (v == null || v.length == 0 || v[0] == -1) return null;
        TreeNode root = new TreeNode(v[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < v.length) {
            TreeNode n = q.poll();
            if (i < v.length && v[i] != -1) { n.left  = new TreeNode(v[i]); q.add(n.left);  } i++;
            if (i < v.length && v[i] != -1) { n.right = new TreeNode(v[i]); q.add(n.right); } i++;
        }
        return root;
    }

    public static void main(String[] args) {
        // [1,2,3,null,null,4,5] roundtrip
        TreeNode root = build(new int[]{1, 2, 3, -1, -1, 4, 5});
        assert inorder(deserialize(serialize(root))).equals(inorder(root));

        // null roundtrip
        assert serialize(null).isEmpty();
        assert deserialize("") == null;
        assert deserialize(null) == null;

        // single node [42]
        TreeNode r = deserialize(serialize(new TreeNode(42)));
        assert r != null && r.val == 42 && r.left == null && r.right == null;

        System.out.println("All tests passed.");
    }
}
