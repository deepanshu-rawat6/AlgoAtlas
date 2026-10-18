import java.util.*;

public class Solution {
    public List<String> findPaths(int[][] maze) {
        int n = maze.length;
        List<String> result = new ArrayList<>();
        if (maze[0][0] == 0) return result;
        boolean[][] visited = new boolean[n][n];
        visited[0][0] = true;
        backtrack(maze, visited, result, new StringBuilder(), 0, 0, n);
        return result;
    }

    private void backtrack(int[][] maze, boolean[][] visited, List<String> result,
                           StringBuilder path, int r, int c, int n) {
        if (r == n - 1 && c == n - 1) {
            result.add(path.toString());
            return;
        }
        // D, L, R, U (lexicographic order)
        int[][] dirs = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
        char[] names = {'D', 'L', 'R', 'U'};
        for (int i = 0; i < 4; i++) {
            int nr = r + dirs[i][0], nc = c + dirs[i][1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && maze[nr][nc] == 1 && !visited[nr][nc]) {
                visited[nr][nc] = true;
                path.append(names[i]);
                backtrack(maze, visited, result, path, nr, nc, n);
                path.deleteCharAt(path.length() - 1);
                visited[nr][nc] = false;
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<String> r = sol.findPaths(new int[][]{{1,0,0,0},{1,1,0,1},{1,1,0,0},{0,1,1,1}});
        assert r.equals(Arrays.asList("DDRDRR", "DRDDRR")) : "wrong: " + r;

        List<String> r2 = sol.findPaths(new int[][]{{0,1},{1,1}});
        assert r2.isEmpty() : "should be empty when start blocked";

        System.out.println("All tests passed.");
    }
}
