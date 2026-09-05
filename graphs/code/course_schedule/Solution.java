// LC 207: Course Schedule
// Cycle detection via DFS coloring: 0=unvisited, 1=visiting, 2=done.
// Time: O(V+E), Space: O(V+E)
import java.util.*;

public class Solution {
    private int[] color;
    private List<List<Integer>> adj;

    private boolean hasCycle(int v) {
        color[v] = 1;
        for (int nb : adj.get(v)) {
            if (color[nb] == 1) return true;
            if (color[nb] == 0 && hasCycle(nb)) return true;
        }
        color[v] = 2;
        return false;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        color = new int[numCourses];
        for (int[] e : prerequisites) adj.get(e[1]).add(e[0]);
        for (int i = 0; i < numCourses; i++)
            if (color[i] == 0 && hasCycle(i)) return false;
        return true;
    }

    public static void main(String[] args) {
        Solution s;

        s = new Solution();
        assert s.canFinish(2, new int[][]{{1,0}}) == true : "Test 1 failed";

        s = new Solution();
        assert s.canFinish(2, new int[][]{{1,0},{0,1}}) == false : "Test 2 failed";

        s = new Solution();
        assert s.canFinish(1, new int[][]{}) == true : "Test 3 failed";

        s = new Solution();
        assert s.canFinish(4, new int[][]{{1,0},{2,0},{3,1},{3,2}}) == true : "Test 4 failed";

        s = new Solution();
        assert s.canFinish(3, new int[][]{{1,0},{2,1},{0,2}}) == false : "Test 5 failed";

        System.out.println("All tests passed.");
    }
}
