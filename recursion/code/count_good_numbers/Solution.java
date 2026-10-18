import java.util.*;

public class Solution {
    private static final long MOD = 1_000_000_007L;

    public int countGoodNumbers(long n) {
        long evenCount = (n + 1) / 2;
        long oddCount = n / 2;
        return (int) (modPow(5, evenCount, MOD) * modPow(4, oddCount, MOD) % MOD);
    }

    private long modPow(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * base % mod;
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.countGoodNumbers(1) == 5 : "test failed";
        assert sol.countGoodNumbers(4) == 400 : "test failed";
        assert sol.countGoodNumbers(50) == 564908303 : "test failed";
        System.out.println("All tests passed.");
    }
}
