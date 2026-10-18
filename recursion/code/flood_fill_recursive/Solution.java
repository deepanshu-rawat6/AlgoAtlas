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
        dfs(image, r + 1, c, original, color);
        dfs(image, r - 1, c, original, color);
        dfs(image, r, c + 1, original, color);
        dfs(image, r, c - 1, original, color);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] img = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
        int[][] result = sol.floodFill(img, 1, 1, 2);
        assert Arrays.deepEquals(result, new int[][]{{2, 2, 2}, {2, 2, 0}, {2, 0, 1}}) : "test failed";

        int[][] img2 = {{0, 0, 0}, {0, 0, 0}};
        assert Arrays.deepEquals(sol.floodFill(img2, 0, 0, 0), new int[][]{{0, 0, 0}, {0, 0, 0}}) : "test failed";

        assert Arrays.deepEquals(sol.floodFill(new int[][]{{1}}, 0, 0, 5), new int[][]{{5}}) : "test failed";
        System.out.println("All tests passed.");
    }
}
