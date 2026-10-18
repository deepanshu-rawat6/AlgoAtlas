import java.util.*;

public class Solution {
    public int reverse(int x) {
        // Extract digits via %10, build reversed number; check 32-bit overflow
        int result = 0;
        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > 7)) return 0;
            if (result < Integer.MIN_VALUE / 10 || (result == Integer.MIN_VALUE / 10 && digit < -8)) return 0;
            result = result * 10 + digit;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.reverse(123) == 321;
        assert sol.reverse(-123) == -321;
        assert sol.reverse(120) == 21;
        assert sol.reverse(1534236469) == 0;   // overflow
        System.out.println("All tests passed.");
    }
}
