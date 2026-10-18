import java.util.*;

public class Solution {
    public void solveSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][10];
        boolean[][] cols = new boolean[9][10];
        boolean[][] boxes = new boolean[9][10];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] != '.') {
                    int d = board[r][c] - '0';
                    rows[r][d] = cols[c][d] = boxes[(r / 3) * 3 + c / 3][d] = true;
                }
            }
        }
        backtrack(board, rows, cols, boxes, 0);
    }

    private boolean backtrack(char[][] board, boolean[][] rows, boolean[][] cols,
                               boolean[][] boxes, int pos) {
        while (pos < 81) {
            int r = pos / 9, c = pos % 9;
            if (board[r][c] == '.') break;
            pos++;
        }
        if (pos == 81) return true;
        int r = pos / 9, c = pos % 9, boxId = (r / 3) * 3 + c / 3;
        for (int d = 1; d <= 9; d++) {
            if (!rows[r][d] && !cols[c][d] && !boxes[boxId][d]) {
                board[r][c] = (char) ('0' + d);
                rows[r][d] = cols[c][d] = boxes[boxId][d] = true;
                if (backtrack(board, rows, cols, boxes, pos + 1)) return true;
                board[r][c] = '.';
                rows[r][d] = cols[c][d] = boxes[boxId][d] = false;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] board = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        sol.solveSudoku(board);
        // Spot-check a known cell in the solution
        assert board[0][2] == '4' : "board[0][2] should be 4, got " + board[0][2];
        assert board[8][0] == '3' : "board[8][0] should be 3, got " + board[8][0];
        // Verify no '.' remains
        for (char[] row : board) for (char ch : row) assert ch != '.' : "unsolved cell";

        System.out.println("All tests passed.");
    }
}
