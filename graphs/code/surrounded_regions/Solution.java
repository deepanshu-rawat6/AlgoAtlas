import java.util.*;

public class Solution {
    // BFS: mark border-connected O's as safe, flip remaining O's to X, restore safe to O
    public void solve(char[][] board) {
        int rows = board.length, cols = board[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if ((r==0||r==rows-1||c==0||c==cols-1) && board[r][c]=='O') {
                    board[r][c] = 'S'; q.add(new int[]{r, c});
                }
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] d : dirs) {
                int nr = cur[0]+d[0], nc = cur[1]+d[1];
                if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&board[nr][nc]=='O') {
                    board[nr][nc] = 'S'; q.add(new int[]{nr, nc});
                }
            }
        }
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                board[r][c] = board[r][c]=='S' ? 'O' : 'X';
    }

    // DFS variant
    public void solveDfs(char[][] board) {
        int rows = board.length, cols = board[0].length;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if ((r==0||r==rows-1||c==0||c==cols-1) && board[r][c]=='O') dfs(board, r, c, rows, cols);
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                board[r][c] = board[r][c]=='S' ? 'O' : 'X';
    }

    private void dfs(char[][] board, int r, int c, int rows, int cols) {
        if (r<0||r>=rows||c<0||c>=cols||board[r][c]!='O') return;
        board[r][c] = 'S';
        dfs(board, r+1, c, rows, cols); dfs(board, r-1, c, rows, cols);
        dfs(board, r, c+1, rows, cols); dfs(board, r, c-1, rows, cols);
    }

    static char[][] copyBoard(char[][] b) {
        char[][] c = new char[b.length][];
        for (int i = 0; i < b.length; i++) c[i] = b[i].clone();
        return c;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        char[][] board = {{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};
        char[][] expected = {{'X','X','X','X'},{'X','X','X','X'},{'X','X','X','X'},{'X','O','X','X'}};
        char[][] b1 = copyBoard(board);
        s.solve(b1);
        assert Arrays.deepEquals(b1, expected) : "test 1";
        char[][] b2 = copyBoard(board);
        s.solveDfs(b2);
        assert Arrays.deepEquals(b2, expected) : "test 2";
        System.out.println("All tests passed.");
    }
}
