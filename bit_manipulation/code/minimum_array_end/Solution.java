import java.util.*;

public class Solution {
    public long minEnd(int n, int x) {
        // Embed bits of (n-1) into the zero-bit positions of x to get minimum last element
        // Use long: result can exceed int range when n and x are both large
        long result = x;
        long remaining = n - 1;
        long bit = 1;
        while (remaining != 0) {
            if ((result & bit) == 0) {      // free bit position (0 in x)
                if ((remaining & 1) == 1) result |= bit;
                remaining >>= 1;
            }
            bit <<= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minEnd(3, 4) == 6;
        assert sol.minEnd(2, 7) == 15;
        assert sol.minEnd(1, 1) == 1;
        assert sol.minEnd(6, 4) == 14;   // nums=[4,5,6,12,13,14]
        System.out.println("All tests passed.");
    }
}
