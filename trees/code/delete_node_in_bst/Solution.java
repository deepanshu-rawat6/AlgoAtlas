import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

public class Solution {

    // O(h) — find node, replace with inorder successor if two children
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) { root.left  = deleteNode(root.left,  key); }
        else if (key > root.val) { root.right = deleteNode(root.right, key); }
        else {
            if (root.left  == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode succ = root.right;
            while (succ.left != null) succ = succ.left;
            root.val   = succ.val;
            root.right = deleteNode(root.right, succ.val);
        }
        return root;
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

    static List<Integer> inorder(TreeNode node) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = node;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop(); res.add(cur.val); cur = cur.right;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode r1 = build(new Integer[]{5,3,6,2,4,null,7});
        assert !inorder(sol.deleteNode(r1, 3)).contains(3);

        TreeNode r2 = build(new Integer[]{5,3,6,2,4,null,7});
        assert inorder(sol.deleteNode(r2, 0)).equals(Arrays.asList(2,3,4,5,6,7));

        assert sol.deleteNode(null, 0) == null;

        System.out.println("All tests passed.");
    }
}
