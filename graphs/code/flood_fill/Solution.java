import java.util.*;

public class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if (original == color) return image;
        dfs(image, sr, sc, original, color);
        return image;
    }

    private void dfs(int[][] image, int r, int c, int original, int color) {
        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length) return;
        if (image[r][c] != original) return;
        image[r][c] = color;
        dfs(image, r+1, c, original, color);
        dfs(image, r-1, c, original, color);
        dfs(image, r, c+1, original, color);
        dfs(image, r, c-1, original, color);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.deepEquals(s.floodFill(new int[][]{{1,1,1},{1,1,0},{1,0,1}}, 1, 1, 2),
            new int[][]{{2,2,2},{2,2,0},{2,0,1}}) : "test 1";
        assert Arrays.deepEquals(s.floodFill(new int[][]{{0,0,0},{0,0,0}}, 0, 0, 0),
            new int[][]{{0,0,0},{0,0,0}}) : "test 2";
        System.out.println("All tests passed.");
    }
}
