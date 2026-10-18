import java.util.*;

public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Check if k nodes remain; if not, leave as-is
        ListNode cur = head;
        int count = 0;
        while (cur != null && count < k) { cur = cur.next; count++; }
        if (count < k) return head;
        // Reverse k nodes
        ListNode prev = null; cur = head;
        for (int i = 0; i < k; i++) {
            ListNode nxt = cur.next; cur.next = prev; prev = cur; cur = nxt;
        }
        // head is now the tail; connect it to the result of the recursive call
        head.next = reverseKGroup(cur, k);
        return prev;
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
        assert Arrays.equals(toArr(sol.reverseKGroup(build(1,2,3,4,5), 2)), new int[]{2,1,4,3,5});
        assert Arrays.equals(toArr(sol.reverseKGroup(build(1,2,3,4,5), 3)), new int[]{3,2,1,4,5});
        assert Arrays.equals(toArr(sol.reverseKGroup(build(1,2,3,4,5), 1)), new int[]{1,2,3,4,5});
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
