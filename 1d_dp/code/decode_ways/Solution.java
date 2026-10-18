import java.util.*;

public class Solution {
    // Space-optimized bottom-up — O(n) time, O(1) space
    public int numDecodings(String s) {
        int n = s.length();
        // next2 = dp[i+2], next1 = dp[i+1]; iterate right to left
        int next2 = 1, next1 = 1;
        for (int i = n - 1; i >= 0; i--) {
            int curr = 0;
            if (s.charAt(i) != '0') {
                curr = next1;
                if (i + 1 < n) {
                    int two = (s.charAt(i) - '0') * 10 + (s.charAt(i + 1) - '0');
                    if (two <= 26) curr += next2;
                }
            }
            next2 = next1;
            next1 = curr;
        }
        return next1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numDecodings("12") == 2 : "12";
        assert sol.numDecodings("226") == 3 : "226";
        assert sol.numDecodings("06") == 0 : "leading zero";
        assert sol.numDecodings("0") == 0 : "zero";
        System.out.println("All tests passed.");
    }
}
