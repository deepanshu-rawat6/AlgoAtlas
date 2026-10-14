import java.util.*;

public class Solution {
    private static final int INF = Integer.MAX_VALUE;

    // Multi-source BFS from all gates simultaneously
    public void wallsAndGates(int[][] rooms) {
        int rows = rooms.length, cols = rooms[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (rooms[r][c] == 0) q.add(new int[]{r, c});
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] d : dirs) {
                int nr = cur[0]+d[0], nc = cur[1]+d[1];
                if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&rooms[nr][nc]==INF) {
                    rooms[nr][nc] = rooms[cur[0]][cur[1]] + 1; q.add(new int[]{nr, nc});
                }
            }
        }
    }

    static int[][] copy(int[][] g) {
        int[][] c = new int[g.length][];
        for (int i = 0; i < g.length; i++) c[i] = g[i].clone();
        return c;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int I = INF;
        int[][] rooms = {{I,-1,0,I},{I,I,I,-1},{I,-1,I,-1},{0,-1,I,I}};
        int[][] expected = {{3,-1,0,1},{2,2,1,-1},{1,-1,2,-1},{0,-1,3,4}};
        int[][] r1 = copy(rooms);
        s.wallsAndGates(r1);
        assert Arrays.deepEquals(r1, expected) : "test 1";
        System.out.println("All tests passed.");
    }
}
