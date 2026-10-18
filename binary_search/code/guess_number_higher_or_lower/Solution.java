import java.util.*;

public class Solution {
    private static int secret;

    private static int guess(int n) {
        if (n > secret) return -1;
        if (n < secret) return 1;
        return 0;
    }

    public int guessNumber(int n) {
        int lo = 1, hi = n;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int res = guess(mid);
            if (res == 0) return mid;
            else if (res == 1) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        secret = 6;
        assert sol.guessNumber(10) == 6 : "test 1 failed";

        secret = 1;
        assert sol.guessNumber(1) == 1 : "test 2 failed";

        secret = 2;
        assert sol.guessNumber(2) == 2 : "test 3 failed";

        secret = 1702766719;
        assert sol.guessNumber(2126753390) == 1702766719 : "test 4 failed";

        System.out.println("All tests passed.");
    }
}
