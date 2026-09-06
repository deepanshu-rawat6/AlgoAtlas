import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    static TreeNode build(int[] v) {
        if (v == null || v.length == 0 || v[0] == -1) return null;
        TreeNode root = new TreeNode(v[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < v.length) {
            TreeNode node = q.poll();
            if (i < v.length && v[i] != -1) { node.left  = new TreeNode(v[i]); q.add(node.left); }  i++;
            if (i < v.length && v[i] != -1) { node.right = new TreeNode(v[i]); q.add(node.right); } i++;
        }
        return root;
    }

    static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        boolean ltr = true;
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left  != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            if (!ltr) Collections.reverse(level);
            res.add(level);
            ltr = !ltr;
        }
        return res;
    }

    public static void main(String[] args) {
        assert zigzagLevelOrder(build(new int[]{3,9,20,-1,-1,15,7}))
            .equals(Arrays.asList(Arrays.asList(3), Arrays.asList(20,9), Arrays.asList(15,7)));
        assert zigzagLevelOrder(null).equals(new ArrayList<>());
        assert zigzagLevelOrder(build(new int[]{1}))
            .equals(Arrays.asList(Arrays.asList(1)));
        System.out.println("All tests passed.");
    }
}
