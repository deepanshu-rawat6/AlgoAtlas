import java.util.*;

public class Solution {
    public boolean hasCycle(ListNode head) {
        // Floyd's: if slow and fast meet, there's a cycle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    private static ListNode buildCycle(int[] vals, int pos) {
        if (vals.length == 0) return null;
        ListNode[] nodes = new ListNode[vals.length];
        for (int i = 0; i < vals.length; i++) nodes[i] = new ListNode(vals[i]);
        for (int i = 0; i < vals.length - 1; i++) nodes[i].next = nodes[i + 1];
        if (pos != -1) nodes[vals.length - 1].next = nodes[pos];
        return nodes[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.hasCycle(buildCycle(new int[]{3,2,0,-4}, 1));
        assert sol.hasCycle(buildCycle(new int[]{1,2}, 0));
        assert !sol.hasCycle(buildCycle(new int[]{1}, -1));
        assert !sol.hasCycle(null);
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
