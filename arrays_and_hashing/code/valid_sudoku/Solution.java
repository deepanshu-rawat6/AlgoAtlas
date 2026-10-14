import java.util.*;

// LC 36: Valid Sudoku
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Single pass: track seen values per row, col, box — O(1) time/space
        Set<String> seen = new HashSet<>();
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.') continue;
                String row = "r" + r + val;
                String col = "c" + c + val;
                String box = "b" + (r/3) + (c/3) + val;
                if (!seen.add(row) || !seen.add(col) || !seen.add(box)) return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        char[][] valid = {
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
        assert s.isValidSudoku(valid) : "test 1";

        char[][] invalid = new char[9][9];
        for (int i = 0; i < 9; i++) invalid[i] = valid[i].clone();
        invalid[0][1] = '5'; // duplicate 5 in row 0
        assert !s.isValidSudoku(invalid) : "test 2";

        System.out.println("All tests passed.");
    }
}
