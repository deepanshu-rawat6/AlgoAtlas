import java.util.*;

class Node {
    boolean val, isLeaf;
    Node topLeft, topRight, bottomLeft, bottomRight;
    Node(boolean v, boolean leaf) { val = v; isLeaf = leaf; }
}

public class Solution {

    // O(n^2 log n) — check uniformity then recurse on 4 quadrants
    public Node construct(int[][] grid) {
        return build(grid, 0, 0, grid.length);
    }
    private Node build(int[][] grid, int r, int c, int size) {
        int first = grid[r][c];
        for (int dr = 0; dr < size; dr++)
            for (int dc = 0; dc < size; dc++)
                if (grid[r+dr][c+dc] != first)
                    return new Node(true, false){{
                        int half = size / 2;
                        topLeft     = build(grid, r,        c,        half);
                        topRight    = build(grid, r,        c + half, half);
                        bottomLeft  = build(grid, r + half, c,        half);
                        bottomRight = build(grid, r + half, c + half, half);
                    }};
        return new Node(first == 1, true);
    }

    // small helper to avoid double-init anonymous class
    private Node buildNode(int[][] grid, int r, int c, int size) {
        int first = grid[r][c];
        boolean uniform = true;
        outer:
        for (int dr = 0; dr < size; dr++)
            for (int dc = 0; dc < size; dc++)
                if (grid[r+dr][c+dc] != first) { uniform = false; break outer; }
        if (uniform) return new Node(first == 1, true);
        int half = size / 2;
        Node node = new Node(true, false);
        node.topLeft     = buildNode(grid, r,        c,        half);
        node.topRight    = buildNode(grid, r,        c + half, half);
        node.bottomLeft  = buildNode(grid, r + half, c,        half);
        node.bottomRight = buildNode(grid, r + half, c + half, half);
        return node;
    }

    public Node constructClean(int[][] grid) { return buildNode(grid, 0, 0, grid.length); }

    public static void main(String[] args) {
        Solution sol = new Solution();

        Node r1 = sol.constructClean(new int[][]{{0,1},{1,0}});
        assert !r1.isLeaf;
        assert r1.topLeft.isLeaf && !r1.topLeft.val;
        assert r1.topRight.isLeaf && r1.topRight.val;

        Node r2 = sol.constructClean(new int[][]{{1,1},{1,1}});
        assert r2.isLeaf && r2.val;

        Node r3 = sol.constructClean(new int[][]{{0}});
        assert r3.isLeaf && !r3.val;

        System.out.println("All tests passed.");
    }
}
