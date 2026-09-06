import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    static void inorder(TreeNode node, List<Integer> out) {
        if (node == null) return;
        inorder(node.left, out);
        out.add(node.val);
        inorder(node.right, out);
    }

    static boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        List<Integer> l1 = new ArrayList<>(), l2 = new ArrayList<>();
        inorder(root1, l1);
        inorder(root2, l2);
        int i = 0, j = l2.size() - 1;
        while (i < l1.size() && j >= 0) {
            int s = l1.get(i) + l2.get(j);
            if (s == target) return true;
            else if (s < target) i++;
            else j--;
        }
        return false;
    }

    public static void main(String[] args) {
        TreeNode t1 = new TreeNode(2);
        t1.left = new TreeNode(1); t1.right = new TreeNode(4);
        TreeNode t2 = new TreeNode(1);
        t2.left = new TreeNode(0); t2.right = new TreeNode(3);
        assert twoSumBSTs(t1, t2, 5)  == true;
        assert twoSumBSTs(t1, t2, 10) == false;

        TreeNode a = new TreeNode(3), b = new TreeNode(4);
        assert twoSumBSTs(a, b, 7) == true;
        assert twoSumBSTs(a, b, 8) == false;
        System.out.println("All tests passed.");
    }
}
