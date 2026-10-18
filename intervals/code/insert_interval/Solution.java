import java.util.*;

public class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0, n = intervals.length;
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i++]);
        }
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);
        while (i < n) result.add(intervals[i++]);
        return result.toArray(new int[0][]);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.deepEquals(sol.insert(new int[][]{{1,3},{6,9}}, new int[]{2,5}), new int[][]{{1,5},{6,9}}) : "test 1 failed";
        assert Arrays.deepEquals(sol.insert(new int[][]{{1,2},{3,5},{6,7},{8,10},{12,16}}, new int[]{4,8}), new int[][]{{1,2},{3,10},{12,16}}) : "test 2 failed";
        assert Arrays.deepEquals(sol.insert(new int[][]{}, new int[]{5,7}), new int[][]{{5,7}}) : "test 3 failed";
        assert Arrays.deepEquals(sol.insert(new int[][]{{1,5}}, new int[]{2,3}), new int[][]{{1,5}}) : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
