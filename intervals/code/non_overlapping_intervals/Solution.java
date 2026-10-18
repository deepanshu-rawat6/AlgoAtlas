import java.util.*;

public class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int removed = 0, prevEnd = Integer.MIN_VALUE;
        for (int[] interval : intervals) {
            if (interval[0] >= prevEnd) {
                prevEnd = interval[1];
            } else {
                removed++;
            }
        }
        return removed;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.eraseOverlapIntervals(new int[][]{{1,2},{2,3},{3,4},{1,3}}) == 1 : "test 1 failed";
        assert sol.eraseOverlapIntervals(new int[][]{{1,2},{1,2},{1,2}}) == 2 : "test 2 failed";
        assert sol.eraseOverlapIntervals(new int[][]{{1,2},{2,3}}) == 0 : "test 3 failed";
        System.out.println("All tests passed.");
    }
}
