import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // O(n) — hashmap for O(1) inorder lookup; pop from postorder end
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Map<Integer,Integer> idx = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) idx.put(inorder[i], i);
        int[] postIdx = {postorder.length - 1};
        return helper(inorder, postorder, idx, postIdx, 0, inorder.length - 1);
    }
    private TreeNode helper(int[] inorder, int[] postorder, Map<Integer,Integer> idx,
                            int[] postIdx, int inLeft, int inRight) {
        if (inLeft > inRight) return null;
        int rootVal = postorder[postIdx[0]--];
        TreeNode root = new TreeNode(rootVal);
        int mid = idx.get(rootVal);
        root.right = helper(inorder, postorder, idx, postIdx, mid + 1, inRight);
        root.left  = helper(inorder, postorder, idx, postIdx, inLeft, mid - 1);
        return root;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r1 = sol.buildTree(new int[]{9,3,15,20,7}, new int[]{9,15,7,20,3});
        assert r1.val == 3 && r1.left.val == 9 && r1.right.val == 20;

        TreeNode r2 = sol.buildTree(new int[]{-1}, new int[]{-1});
        assert r2.val == -1 && r2.left == null && r2.right == null;

        TreeNode r3 = sol.buildTree(new int[]{2,1,3}, new int[]{2,3,1});
        assert r3.val == 1 && r3.left.val == 2 && r3.right.val == 3;

        System.out.println("All tests passed.");
    }
}
