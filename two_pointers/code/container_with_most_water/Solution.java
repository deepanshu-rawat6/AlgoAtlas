// LC 11: Container With Most Water
// Two pointers from both ends; move the shorter side inward.
// Time: O(n), Space: O(1)
import java.util.*;

public class Solution {
    // Brute: O(n^2) try every pair
    public int maxAreaBrute(int[] height) {
        int res = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i + 1; j < height.length; j++)
                res = Math.max(res, Math.min(height[i], height[j]) * (j - i));
        return res;
    }

    // Optimal: O(n) two pointers
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1, res = 0;
        while (l < r) {
            res = Math.max(res, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]) l++;
            else r--;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}) == 49 : "Test 1 failed";
        assert s.maxArea(new int[]{1, 1}) == 1 : "Test 2 failed";
        assert s.maxArea(new int[]{4, 3, 2, 1, 4}) == 16 : "Test 3 failed";
        assert s.maxArea(new int[]{1, 2, 1}) == 2 : "Test 4 failed";
        System.out.println("All tests passed.");
    }
}
