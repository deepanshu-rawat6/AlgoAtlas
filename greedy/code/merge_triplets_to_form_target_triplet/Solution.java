import java.util.*;

public class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int[] result = new int[3];
        for (int[] t : triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                result[0] = Math.max(result[0], t[0]);
                result[1] = Math.max(result[1], t[1]);
                result[2] = Math.max(result[2], t[2]);
            }
        }
        return Arrays.equals(result, target);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.mergeTriplets(new int[][]{{2,5,3},{1,8,4},{1,7,5}}, new int[]{2,7,5}) == true;
        assert sol.mergeTriplets(new int[][]{{3,4,5},{4,5,6}}, new int[]{3,2,5}) == false;
        assert sol.mergeTriplets(new int[][]{{2,5,3},{2,3,4},{1,2,5}}, new int[]{2,5,5}) == true;
        assert sol.mergeTriplets(new int[][]{{1,1,1}}, new int[]{1,1,1}) == true;
        System.out.println("All tests passed.");
    }
}
