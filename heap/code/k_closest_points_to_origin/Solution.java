import java.util.*;

public class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Max-heap of size k by squared distance; evict farthest when over k
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0]*b[0]+b[1]*b[1] - (a[0]*a[0]+a[1]*a[1]));
        for (int[] p : points) {
            heap.offer(p);
            if (heap.size() > k) heap.poll();
        }
        return heap.toArray(new int[0][]);
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[][] res1 = s.kClosest(new int[][]{{1,3},{-2,2}}, 1);
        assert res1.length == 1 && res1[0][0] == -2 && res1[0][1] == 2;

        int[][] res2 = s.kClosest(new int[][]{{3,3},{5,-1},{-2,4}}, 2);
        assert res2.length == 2;
        // Verify both results have dist^2 <= dist^2 of excluded point (dist^2 of [5,-1] = 26)
        for (int[] p : res2) assert p[0]*p[0]+p[1]*p[1] <= 26;

        int[][] res3 = s.kClosest(new int[][]{{0,0},{1,0}}, 1);
        assert res3[0][0] == 0 && res3[0][1] == 0;

        System.out.println("All tests passed.");
    }
}
