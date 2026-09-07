import java.util.*;

public class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length, total = 0;
        for (int p : cardPoints) total += p;
        int window = n - k;
        if (window == 0) return total;
        int curr = 0;
        for (int i = 0; i < window; i++) curr += cardPoints[i];
        int minMid = curr;
        for (int i = window; i < n; i++) {
            curr += cardPoints[i] - cardPoints[i - window];
            minMid = Math.min(minMid, curr);
        }
        return total - minMid;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxScore(new int[]{1,2,3,4,5,6,1}, 3) == 12;
        assert sol.maxScore(new int[]{2,2,2}, 2) == 4;
        assert sol.maxScore(new int[]{9,7,7,9,7,7,9}, 7) == 55;
        System.out.println("All tests passed.");
    }
}
