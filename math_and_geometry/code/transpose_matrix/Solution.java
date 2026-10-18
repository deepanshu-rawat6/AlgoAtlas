import java.util.*;

public class Solution {
    public int[][] transpose(int[][] matrix) {
        // result[j][i] = matrix[i][j] — O(m*n) time and space
        int m = matrix.length, n = matrix[0].length;
        int[][] result = new int[n][m];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                result[c][r] = matrix[r][c];
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.deepEquals(sol.transpose(new int[][]{{1,2,3},{4,5,6},{7,8,9}}),
                new int[][]{{1,4,7},{2,5,8},{3,6,9}});
        assert Arrays.deepEquals(sol.transpose(new int[][]{{1,2,3},{4,5,6}}),
                new int[][]{{1,4},{2,5},{3,6}});
        assert Arrays.deepEquals(sol.transpose(new int[][]{{1}}), new int[][]{{1}});
        System.out.println("All tests passed.");
    }
}
