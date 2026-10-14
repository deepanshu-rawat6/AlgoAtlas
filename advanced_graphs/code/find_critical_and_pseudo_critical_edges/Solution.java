import java.util.*;

public class Solution {
    // LC 1489: Critical and Pseudo-Critical Edges in MST
    // Kruskal per edge: skip → critical if MST grows; force → pseudo-critical if MST same
    // O(E^2 * alpha(n))
    private int n;
    private int[][] indexed; // [weight, u, v, origIdx]

    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        this.n = n;
        indexed = new int[edges.length][4];
        for (int i = 0; i < edges.length; i++) {
            indexed[i] = new int[]{edges[i][2], edges[i][0], edges[i][1], i};
        }
        Arrays.sort(indexed, Comparator.comparingInt(a -> a[0]));

        int base = kruskal(-1, -1);
        List<Integer> critical = new ArrayList<>(), pseudo = new ArrayList<>();
        for (int i = 0; i < indexed.length; i++) {
            if (kruskal(i, -1) > base) critical.add(indexed[i][3]);
            else if (kruskal(-1, i) == base) pseudo.add(indexed[i][3]);
        }
        Collections.sort(critical); Collections.sort(pseudo);
        return List.of(critical, pseudo);
    }

    private int kruskal(int skipIdx, int forceIdx) {
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int weight = 0, cnt = 0;
        if (forceIdx != -1) {
            union(parent, rank, indexed[forceIdx][1], indexed[forceIdx][2]);
            weight += indexed[forceIdx][0]; cnt++;
        }
        for (int i = 0; i < indexed.length; i++) {
            if (i == skipIdx) continue;
            if (union(parent, rank, indexed[i][1], indexed[i][2])) {
                weight += indexed[i][0]; cnt++;
            }
        }
        return cnt == n - 1 ? weight : Integer.MAX_VALUE;
    }

    private int find(int[] p, int x) {
        while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
        return x;
    }

    private boolean union(int[] p, int[] rank, int x, int y) {
        int px = find(p, x), py = find(p, y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
        p[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<Integer>> r1 = s.findCriticalAndPseudoCriticalEdges(5, new int[][]{{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}});
        assert r1.equals(List.of(List.of(0,1), List.of(2,3,4,5))) : r1;
        List<List<Integer>> r2 = s.findCriticalAndPseudoCriticalEdges(4, new int[][]{{0,1,1},{1,2,1},{0,2,1},{2,3,1}});
        assert r2.equals(List.of(List.of(3), List.of(0,1,2))) : r2;
        System.out.println("All tests passed.");
    }
}
