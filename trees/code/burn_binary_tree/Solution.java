import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // DFS builds parent map + finds start node, then BFS spreads fire — O(n)
    public int amountOfTime(TreeNode root, int start) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        TreeNode[] startNode = {null};
        buildParents(root, null, start, parent, startNode);

        Set<TreeNode> visited = new HashSet<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(startNode[0]);
        visited.add(startNode[0]);
        int time = -1;

        while (!queue.isEmpty()) {
            time++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                for (TreeNode nb : new TreeNode[]{node.left, node.right, parent.get(node)}) {
                    if (nb != null && !visited.contains(nb)) {
                        visited.add(nb);
                        queue.add(nb);
                    }
                }
            }
        }
        return time;
    }

    private void buildParents(TreeNode node, TreeNode par, int start,
                               Map<TreeNode, TreeNode> parent, TreeNode[] startNode) {
        if (node == null) return;
        parent.put(node, par);
        if (node.val == start) startNode[0] = node;
        buildParents(node.left,  node, start, parent, startNode);
        buildParents(node.right, node, start, parent, startNode);
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
        assert sol.amountOfTime(build(new Integer[]{1,5,3,null,4,10,6,9,2}), 3) == 4;
        assert sol.amountOfTime(build(new Integer[]{1}), 1) == 0;
        assert sol.amountOfTime(build(new Integer[]{1,2}), 2) == 2;
        System.out.println("All tests passed.");
    }
}
