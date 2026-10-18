import java.util.*;

public class Solution {
    public void rotate(int[][] matrix) {
        // 90° clockwise = transpose + reverse each row — O(n^2), O(1) space
        int n = matrix.length;
        // Transpose
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        // Reverse each row
        for (int[] row : matrix) {
            int lo = 0, hi = n - 1;
            while (lo < hi) { int tmp = row[lo]; row[lo++] = row[hi]; row[hi--] = tmp; }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] m1 = {{1,2,3},{4,5,6},{7,8,9}};
        sol.rotate(m1);
        assert Arrays.deepEquals(m1, new int[][]{{7,4,1},{8,5,2},{9,6,3}});

        int[][] m2 = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
        sol.rotate(m2);
        assert Arrays.deepEquals(m2, new int[][]{{15,13,2,5},{14,3,4,1},{12,6,8,9},{16,7,10,11}});

        int[][] m3 = {{1}};
        sol.rotate(m3);
        assert Arrays.deepEquals(m3, new int[][]{{1}});

        System.out.println("All tests passed.");
    }
}
