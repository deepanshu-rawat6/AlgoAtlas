import java.util.*;

public class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer,Integer> count = new HashMap<>();
        int left = 0, result = 0;
        for (int right = 0; right < fruits.length; right++) {
            count.merge(fruits[right], 1, Integer::sum);
            while (count.size() > 2) {
                int lf = fruits[left++];
                if (count.merge(lf, -1, Integer::sum) == 0) count.remove(lf);
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.totalFruit(new int[]{1,2,1}) == 3;
        assert sol.totalFruit(new int[]{0,1,2,2}) == 3;
        assert sol.totalFruit(new int[]{1,2,3,2,2}) == 4;
        System.out.println("All tests passed.");
    }
}
