import java.util.*;

public class Solution {
    // Rolling three variables — O(n) time, O(1) space
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n <= 2) return 1;
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            int d = a + b + c;
            a = b; b = c; c = d;
        }
        return c;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.tribonacci(0) == 0 : "T(0)";
        assert sol.tribonacci(1) == 1 : "T(1)";
        assert sol.tribonacci(4) == 4 : "T(4)";
        assert sol.tribonacci(25) == 1389537 : "T(25)";
        System.out.println("All tests passed.");
    }
}
