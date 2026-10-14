import java.util.*;

public class Solution {
    // Reverse BFS from each ocean's border inward; intersection = answer
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        Queue<int[]> pacQ = new ArrayDeque<>(), atlQ = new ArrayDeque<>();
        boolean[][] pac = new boolean[rows][cols], atl = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            pacQ.add(new int[]{r, 0});   pac[r][0] = true;
            atlQ.add(new int[]{r, cols-1}); atl[r][cols-1] = true;
        }
        for (int c = 0; c < cols; c++) {
            pacQ.add(new int[]{0, c});   pac[0][c] = true;
            atlQ.add(new int[]{rows-1, c}); atl[rows-1][c] = true;
        }
        bfs(heights, pacQ, pac, rows, cols);
        bfs(heights, atlQ, atl, rows, cols);
        List<List<Integer>> res = new ArrayList<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (pac[r][c] && atl[r][c]) res.add(Arrays.asList(r, c));
        return res;
    }

    private void bfs(int[][] h, Queue<int[]> q, boolean[][] visited, int rows, int cols) {
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] d : dirs) {
                int nr = cur[0]+d[0], nc = cur[1]+d[1];
                if (nr>=0 && nr<rows && nc>=0 && nc<cols && !visited[nr][nc] && h[nr][nc]>=h[cur[0]][cur[1]]) {
                    visited[nr][nc] = true; q.add(new int[]{nr, nc});
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] h = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(0,4), Arrays.asList(1,3), Arrays.asList(1,4),
            Arrays.asList(2,2), Arrays.asList(3,0), Arrays.asList(3,1), Arrays.asList(4,0)
        );
        assert s.pacificAtlantic(h).equals(expected) : "test 1";
        assert s.pacificAtlantic(new int[][]{{1}}).equals(Arrays.asList(Arrays.asList(0,0))) : "test 2";
        System.out.println("All tests passed.");
    }
}
