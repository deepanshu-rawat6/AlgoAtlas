import java.util.*;

public class Solution {
    private long hoursNeeded(int[] piles, int k) {
        long hours = 0;
        for (int p : piles) {
            hours += (p + k - 1) / k;  // ceil(p/k)
        }
        return hours;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (hoursNeeded(piles, mid) <= h) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minEatingSpeed(new int[]{3,6,7,11}, 8) == 4 : "test 1 failed";
        assert sol.minEatingSpeed(new int[]{30,11,23,4,20}, 5) == 30 : "test 2 failed";
        assert sol.minEatingSpeed(new int[]{30,11,23,4,20}, 6) == 23 : "test 3 failed";
        assert sol.minEatingSpeed(new int[]{1000000000}, 1000000000) == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
