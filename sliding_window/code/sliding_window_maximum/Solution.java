import java.util.*;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        int ri = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.addLast(i);
            if (dq.peekFirst() < i - k + 1) dq.pollFirst();
            if (i >= k - 1) result[ri++] = nums[dq.peekFirst()];
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(sol.maxSlidingWindow(new int[]{1,3,-1,-3,5,3,6,7}, 3), new int[]{3,3,5,5,6,7});
        assert Arrays.equals(sol.maxSlidingWindow(new int[]{1}, 1), new int[]{1});
        assert Arrays.equals(sol.maxSlidingWindow(new int[]{1,-1}, 1), new int[]{1,-1});
        System.out.println("All tests passed.");
    }
}
