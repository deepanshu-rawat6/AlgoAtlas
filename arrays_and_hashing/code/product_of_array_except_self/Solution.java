import java.util.*;

// LC 238: Product of Array Except Self
public class Solution {
    public int[] productExceptSelfBrute(int[] nums) {
        // O(n^2): for each index multiply all others
        int n = nums.length;
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int p = 1;
            for (int j = 0; j < n; j++)
                if (j != i) p *= nums[j];
            answer[i] = p;
        }
        return answer;
    }

    public int[] productExceptSelf(int[] nums) {
        // Two-pass: left product then right product — O(n) time, O(1) extra space
        int n = nums.length;
        int[] answer = new int[n];
        Arrays.fill(answer, 1);
        int prefix = 1;
        for (int i = 0; i < n; i++) { answer[i] = prefix; prefix *= nums[i]; }
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) { answer[i] *= suffix; suffix *= nums[i]; }
        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.productExceptSelf(new int[]{1,2,3,4}), new int[]{24,12,8,6}) : "test 1";
        assert Arrays.equals(s.productExceptSelf(new int[]{-1,1,0,-3,3}), new int[]{0,0,9,0,0}) : "test 2";
        assert Arrays.equals(s.productExceptSelf(new int[]{1,1}), new int[]{1,1}) : "test 3";
        System.out.println("All tests passed.");
    }
}
