import java.util.*;

public class Solution {
    // LC 1334: Find City With Smallest Neighbors at Threshold Distance
    // Floyd-Warshall all-pairs shortest paths; tie-break toward larger index — O(n^3)
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int INF = Integer.MAX_VALUE / 2;
        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, INF);
        for (int i = 0; i < n; i++) dist[i][i] = 0;
        for (int[] e : edges) { dist[e[0]][e[1]] = e[2]; dist[e[1]][e[0]] = e[2]; }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];

        int bestCity = -1, minCount = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) if (i != j && dist[i][j] <= distanceThreshold) count++;
            if (count <= minCount) { minCount = count; bestCity = i; }
        }
        return bestCity;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findTheCity(4, new int[][]{{0,1,3},{1,2,1},{1,3,4},{2,3,1}}, 4) == 3 : "t1";
        assert s.findTheCity(5, new int[][]{{0,1,2},{0,4,8},{1,2,3},{1,4,2},{2,3,1},{3,4,1}}, 2) == 0 : "t2";
        assert s.findTheCity(2, new int[][]{}, 0) == 1 : "t3";
        System.out.println("All tests passed.");
    }
}
