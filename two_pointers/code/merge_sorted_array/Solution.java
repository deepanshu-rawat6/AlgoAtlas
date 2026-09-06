import java.util.Arrays;

public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
            else nums1[k--] = nums2[j--];
        }
        while (j >= 0) nums1[k--] = nums2[j--];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] a = {1,2,3,0,0,0};
        sol.merge(a, 3, new int[]{2,5,6}, 3);
        assert Arrays.equals(a, new int[]{1,2,2,3,5,6});
        int[] b = {1};
        sol.merge(b, 1, new int[]{}, 0);
        assert Arrays.equals(b, new int[]{1});
        int[] c = {0};
        sol.merge(c, 0, new int[]{1}, 1);
        assert Arrays.equals(c, new int[]{1});
        System.out.println("All tests passed.");
    }
}
