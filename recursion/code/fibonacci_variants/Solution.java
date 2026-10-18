import java.util.*;

public class Solution {
    public long fibNaive(int n) {
        if (n <= 1) return n;
        return fibNaive(n - 1) + fibNaive(n - 2);
    }

    public long fib(int n) {
        Map<Integer, Long> memo = new HashMap<>();
        return fibMemo(n, memo);
    }

    private long fibMemo(int n, Map<Integer, Long> memo) {
        if (n <= 1) return n;
        if (memo.containsKey(n)) return memo.get(n);
        long result = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    public long fibIterative(int n) {
        if (n <= 1) return n;
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long tmp = a + b;
            a = b;
            b = tmp;
        }
        return b;
    }

    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int tmp = a + b;
            a = b;
            b = tmp;
        }
        return b;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.fib(10) == 55 : "test failed";
        assert sol.fibNaive(10) == 55 : "test failed";
        assert sol.fibIterative(10) == 55 : "test failed";
        assert sol.climbStairs(5) == 8 : "test failed";
        assert sol.climbStairs(1) == 1 : "test failed";
        assert sol.climbStairs(2) == 2 : "test failed";
        System.out.println("All tests passed.");
    }
}
