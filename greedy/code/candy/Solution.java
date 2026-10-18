import java.util.*;

public class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        // Left pass: right neighbor with higher rating gets more
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        // Right pass: left neighbor with higher rating gets more
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
        }
        int sum = 0;
        for (int c : candies) sum += c;
        return sum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.candy(new int[]{1, 0, 2}) == 5;
        assert sol.candy(new int[]{1, 2, 2}) == 4;
        assert sol.candy(new int[]{1}) == 1;
        assert sol.candy(new int[]{1, 3, 2, 2, 1}) == 7;
        System.out.println("All tests passed.");
    }
}
