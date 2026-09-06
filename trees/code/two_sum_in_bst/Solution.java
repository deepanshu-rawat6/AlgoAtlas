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

    static void inorder(TreeNode node, List<Integer> out) {
        if (node == null) return;
        inorder(node.left, out);
        out.add(node.val);
        inorder(node.right, out);
    }

    static boolean findTarget(TreeNode root, int k) {
        List<Integer> nums = new ArrayList<>();
        inorder(root, nums);
        int lo = 0, hi = nums.size() - 1;
        while (lo < hi) {
            int s = nums.get(lo) + nums.get(hi);
            if (s == k) return true;
            else if (s < k) lo++;
            else hi--;
        }
        return false;
    }

    public static void main(String[] args) {
        assert findTarget(build(new int[]{5,3,6,2,4,-1,7}), 9)  == true;
        assert findTarget(build(new int[]{5,3,6,2,4,-1,7}), 28) == false;
        assert findTarget(build(new int[]{1,-1,2}), 3)          == true;
        System.out.println("All tests passed.");
    }
}
