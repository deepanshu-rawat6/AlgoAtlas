import java.util.*;

public class Solution {
    public int getSum(int a, int b) {
        // XOR gives sum without carry; AND<<1 gives carry; repeat until no carry
        // Java int is 32-bit signed — no mask needed unlike Python's arbitrary precision
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.getSum(1, 2) == 3;
        assert sol.getSum(2, 3) == 5;
        assert sol.getSum(-1, 1) == 0;
        assert sol.getSum(-5, 3) == -2;
        System.out.println("All tests passed.");
    }
}
