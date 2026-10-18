import java.util.*;

public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), cur = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) { cur.next = l1; l1 = l1.next; }
            else { cur.next = l2; l2 = l2.next; }
            cur = cur.next;
        }
        cur.next = l1 != null ? l1 : l2;
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
        assert Arrays.equals(toArr(sol.mergeTwoLists(build(1,2,4), build(1,3,4))), new int[]{1,1,2,3,4,4});
        assert sol.mergeTwoLists(null, null) == null;
        assert Arrays.equals(toArr(sol.mergeTwoLists(null, build(0))), new int[]{0});
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
