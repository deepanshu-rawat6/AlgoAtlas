import java.util.*;

public class Solution {
    // Binary search (patience sorting) — O(n log n) time, O(n) space
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int num : nums) {
            int lo = 0, hi = size;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (tails[mid] < num) lo = mid + 1;
                else hi = mid;
            }
            tails[lo] = num;
            if (lo == size) size++;
        }
        return size;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}) == 4 : "example1";
        assert sol.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3}) == 4 : "example2";
        assert sol.lengthOfLIS(new int[]{7, 7, 7, 7}) == 1 : "all same";
        assert sol.lengthOfLIS(new int[]{1}) == 1 : "single";
        System.out.println("All tests passed.");
    }
}
