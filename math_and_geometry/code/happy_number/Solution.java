import java.util.*;

public class Solution {
    private int sumOfSquares(int n) {
        int total = 0;
        while (n > 0) {
            int d = n % 10;
            total += d * d;
            n /= 10;
        }
        return total;
    }

    public boolean isHappy(int n) {
        // Floyd's cycle detection: if we reach 1 it's happy, if slow==fast it's a cycle
        // O(log n) per step, O(1) space
        int slow = n, fast = sumOfSquares(n);
        while (fast != 1 && slow != fast) {
            slow = sumOfSquares(slow);
            fast = sumOfSquares(sumOfSquares(fast));
        }
        return fast == 1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.isHappy(19);
        assert !sol.isHappy(2);
        assert sol.isHappy(1);
        assert !sol.isHappy(4);
        System.out.println("All tests passed.");
    }
}
