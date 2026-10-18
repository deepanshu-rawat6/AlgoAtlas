import java.util.*;

public class Solution {
    public int totalNQueens(int n) {
        boolean[] usedCols = new boolean[n];
        boolean[] usedDiag1 = new boolean[2 * n];
        boolean[] usedDiag2 = new boolean[2 * n];
        return backtrack(usedCols, usedDiag1, usedDiag2, 0, n);
    }

    private int backtrack(boolean[] usedCols, boolean[] usedDiag1, boolean[] usedDiag2, int row, int n) {
        if (row == n) return 1;
        int count = 0;
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n, d2 = row + col;
            if (usedCols[col] || usedDiag1[d1] || usedDiag2[d2]) continue;
            usedCols[col] = usedDiag1[d1] = usedDiag2[d2] = true;
            count += backtrack(usedCols, usedDiag1, usedDiag2, row + 1, n);
            usedCols[col] = usedDiag1[d1] = usedDiag2[d2] = false;
        }
        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.totalNQueens(4) == 2 : "n=4 should be 2";
        assert sol.totalNQueens(1) == 1 : "n=1 should be 1";
        assert sol.totalNQueens(8) == 92 : "n=8 should be 92";

        System.out.println("All tests passed.");
    }
}
