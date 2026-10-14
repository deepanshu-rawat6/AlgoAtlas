import java.util.*;

// LC 304: Range Sum Query 2D - Immutable — 2D prefix sum
class NumMatrix {
    private int[][] prefix;

    NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        prefix = new int[m + 1][n + 1];
        for (int r = 1; r <= m; r++)
            for (int c = 1; c <= n; c++)
                prefix[r][c] = matrix[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1];
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1];
    }
}

public class Solution {
    public static void main(String[] args) {
        int[][] matrix = {
            {3,0,1,4,2},
            {5,6,3,2,1},
            {1,2,0,1,5},
            {4,1,0,1,7},
            {1,0,3,0,5}
        };
        NumMatrix nm = new NumMatrix(matrix);
        assert nm.sumRegion(2,1,4,3) == 8  : "test 1";
        assert nm.sumRegion(1,1,2,2) == 11 : "test 2";
        assert nm.sumRegion(1,2,2,4) == 12 : "test 3";
        System.out.println("All tests passed.");
    }
}
