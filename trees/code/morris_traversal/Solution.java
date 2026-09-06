import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    public List<Integer> morrisInorder(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left == null) {
                res.add(curr.val);
                curr = curr.right;
            } else {
                TreeNode pred = curr.left;
                while (pred.right != null && pred.right != curr)
                    pred = pred.right;
                if (pred.right == null) {
                    pred.right = curr;
                    curr = curr.left;
                } else {
                    pred.right = null;
                    res.add(curr.val);
                    curr = curr.right;
                }
            }
        }
        return res;
    }

    public List<Integer> morrisPreorder(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left == null) {
                res.add(curr.val);
                curr = curr.right;
            } else {
                TreeNode pred = curr.left;
                while (pred.right != null && pred.right != curr)
                    pred = pred.right;
                if (pred.right == null) {
                    res.add(curr.val); // before going left
                    pred.right = curr;
                    curr = curr.left;
                } else {
                    pred.right = null;
                    curr = curr.right;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r = new TreeNode(1);
        r.left = new TreeNode(2); r.right = new TreeNode(3);
        r.left.left = new TreeNode(4); r.left.right = new TreeNode(5);
        assert sol.morrisInorder(r).equals(Arrays.asList(4,2,5,1,3))  : "inorder failed";
        assert sol.morrisPreorder(r).equals(Arrays.asList(1,2,4,5,3)) : "preorder failed";

        TreeNode s = new TreeNode(1);
        assert sol.morrisInorder(s).equals(Arrays.asList(1))  : "single inorder failed";
        assert sol.morrisPreorder(s).equals(Arrays.asList(1)) : "single preorder failed";

        TreeNode rs = new TreeNode(1);
        rs.right = new TreeNode(2); rs.right.right = new TreeNode(3);
        assert sol.morrisInorder(rs).equals(Arrays.asList(1,2,3))  : "right-skewed inorder failed";
        assert sol.morrisPreorder(rs).equals(Arrays.asList(1,2,3)) : "right-skewed preorder failed";

        System.out.println("All tests passed.");
    }
}
