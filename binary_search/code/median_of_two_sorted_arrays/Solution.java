import java.util.*;

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Binary search on partition of smaller array
        // O(log(min(m,n))) time | O(1) space
        if (nums1.length > nums2.length) {
            int[] tmp = nums1; nums1 = nums2; nums2 = tmp;
        }
        int m = nums1.length, n = nums2.length;
        int half = (m + n) / 2;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = lo + (hi - lo) / 2;
            int j = half - i;

            int left1  = (i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int right1 = (i < m) ? nums1[i]     : Integer.MAX_VALUE;
            int left2  = (j > 0) ? nums2[j - 1] : Integer.MIN_VALUE;
            int right2 = (j < n) ? nums2[j]      : Integer.MAX_VALUE;

            if (left1 <= right2 && left2 <= right1) {
                if ((m + n) % 2 == 1) {
                    return Math.min(right1, right2);
                }
                return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
            } else if (left1 > right2) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }
        return 0.0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findMedianSortedArrays(new int[]{1,3}, new int[]{2}) == 2.0 : "test 1 failed";
        assert sol.findMedianSortedArrays(new int[]{1,2}, new int[]{3,4}) == 2.5 : "test 2 failed";
        assert sol.findMedianSortedArrays(new int[]{}, new int[]{1}) == 1.0 : "test 3 failed";
        assert sol.findMedianSortedArrays(new int[]{1,2,3}, new int[]{4,5,6,7}) == 4.0 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
