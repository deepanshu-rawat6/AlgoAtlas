import java.util.*;

public class Solution {
    private int daysNeeded(int[] weights, int cap) {
        int days = 1, load = 0;
        for (int w : weights) {
            if (load + w > cap) {
                days++;
                load = 0;
            }
            load += w;
        }
        return days;
    }

    public int shipWithinDays(int[] weights, int days) {
        int lo = 0, hi = 0;
        for (int w : weights) {
            lo = Math.max(lo, w);
            hi += w;
        }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (daysNeeded(weights, mid) <= days) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.shipWithinDays(new int[]{1,2,3,4,5,6,7,8,9,10}, 5) == 15 : "test 1 failed";
        assert sol.shipWithinDays(new int[]{3,2,2,4,1,4}, 3) == 6 : "test 2 failed";
        assert sol.shipWithinDays(new int[]{1,2,3,1,1}, 4) == 3 : "test 3 failed";
        assert sol.shipWithinDays(new int[]{1}, 1) == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
