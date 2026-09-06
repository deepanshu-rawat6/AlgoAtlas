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

    static List<List<Integer>> verticalTraversal(TreeNode root) {
        if (root == null) return new ArrayList<>();
        // collect [col, row, val]
        List<int[]> nodes = new ArrayList<>();
        Queue<Object[]> q = new LinkedList<>();
        q.add(new Object[]{root, 0, 0});
        while (!q.isEmpty()) {
            Object[] cur = q.poll();
            TreeNode node = (TreeNode) cur[0];
            int col = (int) cur[1], row = (int) cur[2];
            nodes.add(new int[]{col, row, node.val});
            if (node.left  != null) q.add(new Object[]{node.left,  col-1, row+1});
            if (node.right != null) q.add(new Object[]{node.right, col+1, row+1});
        }
        nodes.sort((a, b) -> a[0] != b[0] ? a[0]-b[0] : a[1] != b[1] ? a[1]-b[1] : a[2]-b[2]);
        TreeMap<Integer, List<Integer>> colMap = new TreeMap<>();
        for (int[] n : nodes) colMap.computeIfAbsent(n[0], k -> new ArrayList<>()).add(n[2]);
        return new ArrayList<>(colMap.values());
    }

    public static void main(String[] args) {
        assert verticalTraversal(build(new int[]{3,9,20,-1,-1,15,7}))
            .equals(Arrays.asList(Arrays.asList(9), Arrays.asList(3,15), Arrays.asList(20), Arrays.asList(7)));
        assert verticalTraversal(build(new int[]{1,2,3,4,5,6,7}))
            .equals(Arrays.asList(Arrays.asList(4), Arrays.asList(2), Arrays.asList(1,5,6), Arrays.asList(3), Arrays.asList(7)));
        assert verticalTraversal(build(new int[]{1}))
            .equals(Arrays.asList(Arrays.asList(1)));
        System.out.println("All tests passed.");
    }
}
