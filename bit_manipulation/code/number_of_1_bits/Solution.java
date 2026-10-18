import java.util.*;

public class Solution {
    public int hammingWeightEachBit(int n) {
        // Check each of 32 bits with mask; use >>> for unsigned right shift
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += n & 1;
            n >>>= 1;
        }
        return count;
    }

    public int hammingWeight(int n) {
        // n&(n-1) clears the lowest set bit; count iterations until n=0
        int count = 0;
        while (n != 0) { n &= n - 1; count++; }
        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.hammingWeightEachBit(11) == 3;   // 1011
        assert sol.hammingWeightEachBit(128) == 1;  // 10000000
        assert sol.hammingWeightEachBit(1) == 1;

        assert sol.hammingWeight(11) == 3;
        assert sol.hammingWeight(128) == 1;
        assert sol.hammingWeight(1) == 1;

        System.out.println("All tests passed.");
    }
}
