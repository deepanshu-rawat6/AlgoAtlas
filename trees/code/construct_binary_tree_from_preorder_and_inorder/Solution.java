import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {
    // HashMap for O(1) inorder lookup; preIdx tracks current preorder position — O(n)
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> idxMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) idxMap.put(inorder[i], i);
        int[] preIdx = {0};
        return helper(preorder, idxMap, preIdx, 0, inorder.length - 1);
    }

    private TreeNode helper(int[] pre, Map<Integer,Integer> idxMap, int[] preIdx, int left, int right) {
        if (left > right) return null;
        int val = pre[preIdx[0]++];
        TreeNode root = new TreeNode(val);
        int mid = idxMap.get(val);
        root.left  = helper(pre, idxMap, preIdx, left,    mid - 1);
        root.right = helper(pre, idxMap, preIdx, mid + 1, right);
        return root;
    }

    static List<Integer> inorder(TreeNode node) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = node;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) { stack.push(curr); curr = curr.left; }
            curr = stack.pop(); res.add(curr.val); curr = curr.right;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode t1 = sol.buildTree(new int[]{3,9,20,15,7}, new int[]{9,3,15,20,7});
        assert inorder(t1).equals(Arrays.asList(9,3,15,20,7)) : inorder(t1);

        TreeNode t2 = sol.buildTree(new int[]{-1}, new int[]{-1});
        assert t2.val == -1 && t2.left == null && t2.right == null;

        TreeNode t3 = sol.buildTree(new int[]{1,2,3}, new int[]{2,1,3});
        assert t3.val == 1 && t3.left.val == 2 && t3.right.val == 3;

        System.out.println("All tests passed.");
    }
}
