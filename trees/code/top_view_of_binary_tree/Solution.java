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

    static List<Integer> topView(TreeNode root) {
        if (root == null) return new ArrayList<>();
        TreeMap<Integer, Integer> colMap = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>();          // [node-as-index via map, col] — use Object queue
        Queue<Object[]> bfs = new LinkedList<>();
        bfs.add(new Object[]{root, 0});
        while (!bfs.isEmpty()) {
            Object[] cur = bfs.poll();
            TreeNode node = (TreeNode) cur[0];
            int col = (int) cur[1];
            colMap.putIfAbsent(col, node.val);
            if (node.left  != null) bfs.add(new Object[]{node.left,  col - 1});
            if (node.right != null) bfs.add(new Object[]{node.right, col + 1});
        }
        return new ArrayList<>(colMap.values());
    }

    public static void main(String[] args) {
        assert topView(build(new int[]{1,2,3,4,5,6,7})).equals(Arrays.asList(4,2,1,3,7));
        assert topView(build(new int[]{1,2,3})).equals(Arrays.asList(2,1,3));
        assert topView(build(new int[]{1})).equals(Arrays.asList(1));
        System.out.println("All tests passed.");
    }
}
