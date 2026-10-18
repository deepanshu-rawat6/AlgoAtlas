import java.util.*;

public class Solution {
    public double myPow(double x, int n) {
        // Fast exponentiation by squaring — O(log n)
        // Use long for n to handle Integer.MIN_VALUE negation safely
        long exp = n;
        if (exp < 0) { x = 1.0 / x; exp = -exp; }
        double result = 1.0;
        while (exp > 0) {
            if ((exp & 1) == 1) result *= x;
            x *= x;
            exp >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Math.abs(sol.myPow(2.0, 10) - 1024.0) < 1e-5;
        assert Math.abs(sol.myPow(2.0, -2) - 0.25) < 1e-5;
        assert Math.abs(sol.myPow(2.0, 0) - 1.0) < 1e-5;
        assert Math.abs(sol.myPow(2.1, 3) - 9.261) < 1e-3;
        System.out.println("All tests passed.");
    }
}
