import java.util.*;

public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0); dummy.next = head;
        ListNode fast = dummy;
        for (int i = 0; i <= n; i++) fast = fast.next;
        ListNode slow = dummy;
        while (fast != null) { slow = slow.next; fast = fast.next; }
        slow.next = slow.next.next;
        return dummy.next;
    }

    private static ListNode build(int... vals) {
        ListNode d = new ListNode(0); ListNode c = d;
        for (int v : vals) { c.next = new ListNode(v); c = c.next; }
        return d.next;
    }
    private static int[] toArr(ListNode h) {
        List<Integer> r = new ArrayList<>();
        while (h != null) { r.add(h.val); h = h.next; }
        return r.stream().mapToInt(x -> x).toArray();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(toArr(sol.removeNthFromEnd(build(1,2,3,4,5), 2)), new int[]{1,2,3,5});
        assert Arrays.equals(toArr(sol.removeNthFromEnd(build(1), 1)), new int[]{});
        assert Arrays.equals(toArr(sol.removeNthFromEnd(build(1,2), 1)), new int[]{1});
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
