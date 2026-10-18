import java.util.*;

public class Solution {
    public int findDuplicate(int[] nums) {
        // Floyd's cycle detection: treat array as linked list (index -> nums[index])
        // Cycle entry point == duplicate value
        int slow = nums[0], fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findDuplicate(new int[]{1,3,4,2,2}) == 2;
        assert sol.findDuplicate(new int[]{3,1,3,4,2}) == 3;
        assert sol.findDuplicate(new int[]{3,3,3,3,3}) == 3;
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
