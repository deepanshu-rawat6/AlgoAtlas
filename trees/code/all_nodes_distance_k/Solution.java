import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // Build parent map, then BFS from target in all 3 directions — O(n)
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        buildParents(root, null, parent);

        List<Integer> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();
        queue.add(target);
        visited.add(target);
        int dist = 0;

        while (!queue.isEmpty()) {
            if (dist == k) {
                for (TreeNode n : queue) result.add(n.val);
                return result;
            }
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
            dist++;
        }
        return result;
    }

    private void buildParents(TreeNode node, TreeNode par, Map<TreeNode, TreeNode> parent) {
        if (node == null) return;
        parent.put(node, par);
        buildParents(node.left, node, parent);
        buildParents(node.right, node, parent);
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

    static TreeNode find(TreeNode node, int val) {
        if (node == null) return null;
        if (node.val == val) return node;
        TreeNode l = find(node.left, val);
        return l != null ? l : find(node.right, val);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode root = build(new Integer[]{3,5,1,6,2,0,8,null,null,7,4});
        List<Integer> res = sol.distanceK(root, find(root, 5), 2);
        Collections.sort(res);
        assert res.equals(Arrays.asList(1,4,7)) : res;

        List<Integer> res2 = sol.distanceK(root, find(root, 5), 0);
        assert res2.equals(Arrays.asList(5)) : res2;

        TreeNode single = new TreeNode(42);
        List<Integer> res3 = sol.distanceK(single, single, 0);
        assert res3.equals(Arrays.asList(42)) : res3;

        System.out.println("All tests passed.");
    }
}
