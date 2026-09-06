import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    private void inorder(TreeNode node, List<Integer> out) {
        if (node == null) return;
        inorder(node.left, out);
        out.add(node.val);
        inorder(node.right, out);
    }

    private List<Integer> mergeSorted(List<Integer> a, List<Integer> b) {
        List<Integer> res = new ArrayList<>();
        int i = 0, j = 0;
        while (i < a.size() && j < b.size())
            res.add(a.get(i) <= b.get(j) ? a.get(i++) : b.get(j++));
        while (i < a.size()) res.add(a.get(i++));
        while (j < b.size()) res.add(b.get(j++));
        return res;
    }

    private TreeNode sortedToBST(List<Integer> nums, int lo, int hi) {
        if (lo > hi) return null;
        int mid = lo + (hi - lo) / 2;
        TreeNode node = new TreeNode(nums.get(mid));
        node.left  = sortedToBST(nums, lo, mid - 1);
        node.right = sortedToBST(nums, mid + 1, hi);
        return node;
    }

    public TreeNode mergeBSTs(TreeNode r1, TreeNode r2) {
        List<Integer> a = new ArrayList<>(), b = new ArrayList<>();
        inorder(r1, a);
        inorder(r2, b);
        List<Integer> merged = mergeSorted(a, b);
        return sortedToBST(merged, 0, merged.size() - 1);
    }

    private List<Integer> toInorder(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorder(root, res);
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r1 = new TreeNode(3);
        r1.left = new TreeNode(1); r1.right = new TreeNode(5);
        TreeNode r2 = new TreeNode(4);
        r2.left = new TreeNode(2); r2.right = new TreeNode(6);
        assert sol.toInorder(sol.mergeBSTs(r1, r2)).equals(Arrays.asList(1,2,3,4,5,6)) : "test1 failed";

        TreeNode r3 = new TreeNode(1);
        r3.right = new TreeNode(2);
        assert sol.toInorder(sol.mergeBSTs(r3, null)).equals(Arrays.asList(1,2)) : "test2 failed";

        assert sol.mergeBSTs(null, null) == null : "test3 failed";

        System.out.println("All tests passed.");
    }
}
