import java.util.*;

public class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for (int card : hand) count.merge(card, 1, Integer::sum);
        while (!count.isEmpty()) {
            int first = count.firstKey();
            int need = count.get(first);
            for (int i = 0; i < groupSize; i++) {
                int key = first + i;
                int val = count.getOrDefault(key, 0);
                if (val < need) return false;
                if (val == need) count.remove(key);
                else count.put(key, val - need);
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.isNStraightHand(new int[]{1, 2, 3, 6, 2, 3, 4, 7, 8}, 3) == true;
        assert sol.isNStraightHand(new int[]{1, 2, 3, 4, 5}, 4) == false;
        assert sol.isNStraightHand(new int[]{1, 2, 3}, 3) == true;
        assert sol.isNStraightHand(new int[]{1}, 1) == true;
        System.out.println("All tests passed.");
    }
}
