import java.util.*;

public class Solution {
    public int reverseBitsSimple(int n) {
        // Shift result left and OR in lowest bit of n, 32 times; >>> for unsigned shift
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>>= 1;
        }
        return result;
    }

    public int reverseBits(int n) {
        // Divide and conquer: swap 16, 8, 4, 2, 1-bit groups
        // Masks work correctly as signed ints via two's complement bit patterns
        n = (n >>> 16) | (n << 16);
        n = ((n & 0xFF00FF00) >>> 8)  | ((n & 0x00FF00FF) << 8);
        n = ((n & 0xF0F0F0F0) >>> 4)  | ((n & 0x0F0F0F0F) << 4);
        n = ((n & 0xCCCCCCCC) >>> 2)  | ((n & 0x33333333) << 2);
        n = ((n & 0xAAAAAAAA) >>> 1)  | ((n & 0x55555555) << 1);
        return n;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // 43261596 = 0b00000010100101000001111010011100 -> 964176192
        assert sol.reverseBitsSimple(43261596) == 964176192;
        assert sol.reverseBitsSimple(0) == 0;
        assert sol.reverseBitsSimple(0xFFFFFFFF) == 0xFFFFFFFF;  // -1 reversed is -1

        assert sol.reverseBits(43261596) == 964176192;
        assert sol.reverseBits(0) == 0;
        assert sol.reverseBits(0xFFFFFFFF) == 0xFFFFFFFF;

        System.out.println("All tests passed.");
    }
}
