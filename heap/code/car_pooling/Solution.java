import java.util.*;

public class Solution {
    // Diff array: add passengers at start, remove at end; check running sum <= capacity
    public boolean carPooling(int[][] trips, int capacity) {
        int[] diff = new int[1001];
        for (int[] trip : trips) {
            diff[trip[1]] += trip[0];
            diff[trip[2]] -= trip[0];
        }
        int current = 0;
        for (int delta : diff) {
            current += delta;
            if (current > capacity) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert !s.carPooling(new int[][]{{2,1,5},{3,3,7}}, 4);
        assert s.carPooling(new int[][]{{2,1,5},{3,3,7}}, 5);
        assert s.carPooling(new int[][]{{3,2,7},{3,7,9},{8,3,9}}, 11);
        assert !s.carPooling(new int[][]{{9,3,4},{9,1,5},{1,1,5}}, 9);
        System.out.println("All tests passed.");
    }
}
