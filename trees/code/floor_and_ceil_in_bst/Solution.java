import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // Floor: largest value <= key — O(h)
    public int floor(TreeNode root, int key) {
        int floorVal = -1;
        while (root != null) {
            if (root.val == key) return root.val;
            if (root.val < key) { floorVal = root.val; root = root.right; }
            else                { root = root.left; }
        }
        return floorVal;
    }

    // Ceil: smallest value >= key — O(h)
    public int ceil(TreeNode root, int key) {
        int ceilVal = -1;
        while (root != null) {
            if (root.val == key) return root.val;
            if (root.val > key) { ceilVal = root.val; root = root.left; }
            else                { root = root.right; }
        }
        return ceilVal;
    }

    static TreeNode build(Integer[] vals) {
        if (vals == null || vals.length == 0) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            TreeNode node = q.poll();
            if (i < vals.length && vals[i] != null) { node.left  = new TreeNode(vals[i]); q.add(node.left);  } i++;
            if (i < vals.length && vals[i] != null) { node.right = new TreeNode(vals[i]); q.add(node.right); } i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        TreeNode root = build(new Integer[]{8,4,12,2,6,10,14});

        assert sol.floor(root, 5) == 4;
        assert sol.ceil(root,  5) == 6;

        assert sol.floor(root, 8) == 8;
        assert sol.ceil(root,  8) == 8;

        assert sol.floor(null, 5) == -1;
        assert sol.ceil(null,  5) == -1;

        System.out.println("All tests passed.");
    }
}
