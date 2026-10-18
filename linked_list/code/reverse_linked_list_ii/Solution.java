import java.util.*;

public class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0); dummy.next = head;
        ListNode pre = dummy;
        for (int i = 0; i < left - 1; i++) pre = pre.next;
        ListNode cur = pre.next;
        // Repeatedly pull cur.next to the front of the reversed segment
        for (int i = 0; i < right - left; i++) {
            ListNode nxt = cur.next;
            cur.next = nxt.next;
            nxt.next = pre.next;
            pre.next = nxt;
        }
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
        assert Arrays.equals(toArr(sol.reverseBetween(build(1,2,3,4,5), 2, 4)), new int[]{1,4,3,2,5});
        assert Arrays.equals(toArr(sol.reverseBetween(build(5), 1, 1)), new int[]{5});
        assert Arrays.equals(toArr(sol.reverseBetween(build(1,2,3,4,5), 1, 5)), new int[]{5,4,3,2,1});
        assert Arrays.equals(toArr(sol.reverseBetween(build(3,5), 1, 2)), new int[]{5,3});
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
