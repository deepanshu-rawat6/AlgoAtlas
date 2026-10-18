import java.util.*;

public class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        // Step 1: find middle
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next; fast = fast.next.next;
        }
        // Step 2: reverse second half
        ListNode prev = null, cur = slow.next;
        slow.next = null;
        while (cur != null) {
            ListNode nxt = cur.next; cur.next = prev; prev = cur; cur = nxt;
        }
        // Step 3: merge first and reversed second half
        ListNode first = head, second = prev;
        while (second != null) {
            ListNode tmp1 = first.next, tmp2 = second.next;
            first.next = second; second.next = tmp1;
            first = tmp1; second = tmp2;
        }
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
        ListNode h1 = build(1,2,3,4);
        sol.reorderList(h1);
        assert Arrays.equals(toArr(h1), new int[]{1,4,2,3});

        ListNode h2 = build(1,2,3,4,5);
        sol.reorderList(h2);
        assert Arrays.equals(toArr(h2), new int[]{1,5,2,4,3});

        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
