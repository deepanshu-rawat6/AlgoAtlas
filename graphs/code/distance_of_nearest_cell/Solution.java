import java.util.*;

public class Solution {
    // Multi-source BFS from all 0-cells simultaneously
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        int[][] dist = new int[rows][cols];
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) q.add(new int[]{r, c});
                else dist[r][c] = Integer.MAX_VALUE;
            }
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && dist[nr][nc] > dist[r][c] + 1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.deepEquals(s.updateMatrix(new int[][]{{0,0,0},{0,1,0},{1,1,1}}),
            new int[][]{{0,0,0},{0,1,0},{1,2,1}}) : "test 1";
        assert Arrays.deepEquals(s.updateMatrix(new int[][]{{0,0,0},{0,1,0},{0,0,0}}),
            new int[][]{{0,0,0},{0,1,0},{0,0,0}}) : "test 2";
        System.out.println("All tests passed.");
    }
}
