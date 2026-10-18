import java.util.*;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), cur = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int val = carry;
            if (l1 != null) { val += l1.val; l1 = l1.next; }
            if (l2 != null) { val += l2.val; l2 = l2.next; }
            carry = val / 10;
            cur.next = new ListNode(val % 10);
            cur = cur.next;
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
        assert Arrays.equals(toArr(sol.addTwoNumbers(build(2,4,3), build(5,6,4))), new int[]{7,0,8});
        assert Arrays.equals(toArr(sol.addTwoNumbers(build(0), build(0))), new int[]{0});
        assert Arrays.equals(toArr(sol.addTwoNumbers(build(9,9,9,9,9,9,9), build(9,9,9,9))), new int[]{8,9,9,9,0,0,0,1});
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
