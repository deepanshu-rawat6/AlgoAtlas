import java.util.*;

// LC 1929: Concatenation of Array
public class Solution {
    public int[] getConcatenationBrute(int[] nums) {
        // Append elements twice via loop — O(n) time, O(n) space
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        return ans;
    }

    public int[] getConcatenation(int[] nums) {
        // System.arraycopy — O(n) time, O(n) space
        int n = nums.length;
        int[] ans = new int[2 * n];
        System.arraycopy(nums, 0, ans, 0, n);
        System.arraycopy(nums, 0, ans, n, n);
        return ans;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.getConcatenation(new int[]{1,2,1}), new int[]{1,2,1,1,2,1}) : "test 1";
        assert Arrays.equals(s.getConcatenation(new int[]{1,3,2,1}), new int[]{1,3,2,1,1,3,2,1}) : "test 2";
        System.out.println("All tests passed.");
    }
}
