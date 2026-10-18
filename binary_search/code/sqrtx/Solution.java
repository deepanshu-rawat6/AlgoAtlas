import java.util.*;

public class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        int lo = 1, hi = x / 2;
        while (lo <= hi) {
            long mid = lo + (hi - lo) / 2;
            long sq = mid * mid;
            if (sq == x) return (int) mid;
            else if (sq < x) lo = (int) mid + 1;
            else hi = (int) mid - 1;
        }
        return hi;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.mySqrt(0) == 0 : "test 1 failed";
        assert sol.mySqrt(1) == 1 : "test 2 failed";
        assert sol.mySqrt(4) == 2 : "test 3 failed";
        assert sol.mySqrt(8) == 2 : "test 4 failed";
        assert sol.mySqrt(9) == 3 : "test 5 failed";
        assert sol.mySqrt(2147395600) == 46340 : "test 6 failed";
        System.out.println("All tests passed.");
    }
}
