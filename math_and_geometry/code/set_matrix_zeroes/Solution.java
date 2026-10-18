import java.util.*;

public class Solution {
    public void setZeroes(int[][] matrix) {
        // Use first row/col as markers — O(m*n) time, O(1) space
        int m = matrix.length, n = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;
        for (int c = 0; c < n; c++) if (matrix[0][c] == 0) { firstRowZero = true; break; }
        for (int r = 0; r < m; r++) if (matrix[r][0] == 0) { firstColZero = true; break; }
        // Mark zeros in first row/col
        for (int r = 1; r < m; r++)
            for (int c = 1; c < n; c++)
                if (matrix[r][c] == 0) { matrix[r][0] = 0; matrix[0][c] = 0; }
        // Apply markers
        for (int r = 1; r < m; r++)
            for (int c = 1; c < n; c++)
                if (matrix[r][0] == 0 || matrix[0][c] == 0) matrix[r][c] = 0;
        if (firstRowZero) for (int c = 0; c < n; c++) matrix[0][c] = 0;
        if (firstColZero) for (int r = 0; r < m; r++) matrix[r][0] = 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] m1 = {{1,1,1},{1,0,1},{1,1,1}};
        sol.setZeroes(m1);
        assert Arrays.deepEquals(m1, new int[][]{{1,0,1},{0,0,0},{1,0,1}});

        int[][] m2 = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        sol.setZeroes(m2);
        assert Arrays.deepEquals(m2, new int[][]{{0,0,0,0},{0,4,5,0},{0,3,1,0}});

        int[][] m3 = {{1,2},{3,4}};
        sol.setZeroes(m3);
        assert Arrays.deepEquals(m3, new int[][]{{1,2},{3,4}});

        System.out.println("All tests passed.");
    }
}
