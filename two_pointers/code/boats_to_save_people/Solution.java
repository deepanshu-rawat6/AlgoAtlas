import java.util.Arrays;

public class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int lo = 0, hi = people.length - 1, boats = 0;
        while (lo <= hi) {
            if (people[lo] + people[hi] <= limit) lo++;
            hi--;
            boats++;
        }
        return boats;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numRescueBoats(new int[]{1, 2}, 3) == 1;
        assert sol.numRescueBoats(new int[]{3, 2, 2, 1}, 3) == 3;
        assert sol.numRescueBoats(new int[]{3, 5, 3, 4}, 5) == 4;
        System.out.println("All tests passed.");
    }
}
