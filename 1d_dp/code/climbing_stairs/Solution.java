import java.util.*;

public class Solution {
    // Space-optimized Fibonacci — O(n) time, O(1) space
    public int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.climbStairs(1) == 1 : "n=1";
        assert sol.climbStairs(2) == 2 : "n=2";
        assert sol.climbStairs(3) == 3 : "n=3";
        assert sol.climbStairs(5) == 8 : "n=5";
        System.out.println("All tests passed.");
    }
}
