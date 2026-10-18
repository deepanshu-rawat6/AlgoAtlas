import java.util.*;

public class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        int[] starts = new int[n], ends = new int[n];
        for (int i = 0; i < n; i++) { starts[i] = intervals[i][0]; ends[i] = intervals[i][1]; }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int rooms = 0, endPtr = 0;
        for (int start : starts) {
            if (start < ends[endPtr]) rooms++;
            else endPtr++;
        }
        return rooms;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minMeetingRooms(new int[][]{{0,30},{5,10},{15,20}}) == 2 : "test 1 failed";
        assert sol.minMeetingRooms(new int[][]{{7,10},{2,4}}) == 1 : "test 2 failed";
        assert sol.minMeetingRooms(new int[][]{{1,5},{2,6},{3,7}}) == 3 : "test 3 failed";
        System.out.println("All tests passed.");
    }
}
