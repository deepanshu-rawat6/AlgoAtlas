import java.util.*;

public class Solution {
    private boolean canSplit(int[] nums, int k, int cap) {
        int parts = 1, curr = 0;
        for (int v : nums) {
            if (curr + v > cap) {
                parts++;
                curr = 0;
            }
            curr += v;
        }
        return parts <= k;
    }

    public int splitArray(int[] nums, int k) {
        int lo = 0, hi = 0;
        for (int v : nums) {
            lo = Math.max(lo, v);
            hi += v;
        }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canSplit(nums, k, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.splitArray(new int[]{7,2,5,10,8}, 2) == 18 : "test 1 failed";
        assert sol.splitArray(new int[]{1,2,3,4,5}, 2) == 9 : "test 2 failed";
        assert sol.splitArray(new int[]{1,4,4}, 3) == 4 : "test 3 failed";
        assert sol.splitArray(new int[]{10}, 1) == 10 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
