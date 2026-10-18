import java.util.*;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        boolean[] usedCols = new boolean[n];
        boolean[] usedDiag1 = new boolean[2 * n]; // row - col + n
        boolean[] usedDiag2 = new boolean[2 * n]; // row + col
        backtrack(result, board, usedCols, usedDiag1, usedDiag2, 0, n);
        return result;
    }

    private void backtrack(List<List<String>> result, char[][] board,
                           boolean[] usedCols, boolean[] usedDiag1, boolean[] usedDiag2,
                           int row, int n) {
        if (row == n) {
            List<String> snapshot = new ArrayList<>();
            for (char[] r : board) snapshot.add(new String(r));
            result.add(snapshot);
            return;
        }
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n, d2 = row + col;
            if (usedCols[col] || usedDiag1[d1] || usedDiag2[d2]) continue;
            board[row][col] = 'Q';
            usedCols[col] = usedDiag1[d1] = usedDiag2[d2] = true;
            backtrack(result, board, usedCols, usedDiag1, usedDiag2, row + 1, n);
            board[row][col] = '.';
            usedCols[col] = usedDiag1[d1] = usedDiag2[d2] = false;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<String>> r4 = sol.solveNQueens(4);
        assert r4.size() == 2 : "n=4 should have 2 solutions";

        List<List<String>> r1 = sol.solveNQueens(1);
        assert r1.size() == 1 && r1.get(0).equals(Collections.singletonList("Q"));

        System.out.println("All tests passed.");
    }
}
