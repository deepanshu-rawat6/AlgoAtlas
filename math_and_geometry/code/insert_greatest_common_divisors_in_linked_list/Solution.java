import java.util.*;

public class Solution {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public ListNode insertGreatestCommonDivisors(ListNode head) {
        // Insert gcd(a, b) node between every adjacent pair — O(n) single pass
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            int g = gcd(cur.val, cur.next.val);
            cur.next = new ListNode(g, cur.next);
            cur = cur.next.next;
        }
        return head;
    }

    private static ListNode fromArray(int[] arr) {
        ListNode dummy = new ListNode(0), cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        return dummy.next;
    }

    private static int[] toArray(ListNode head) {
        List<Integer> list = new ArrayList<>();
        while (head != null) { list.add(head.val); head = head.next; }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(toArray(sol.insertGreatestCommonDivisors(fromArray(new int[]{18, 6, 10, 3}))),
                new int[]{18, 6, 6, 2, 10, 1, 3});
        assert Arrays.equals(toArray(sol.insertGreatestCommonDivisors(fromArray(new int[]{7}))),
                new int[]{7});
        assert Arrays.equals(toArray(sol.insertGreatestCommonDivisors(fromArray(new int[]{4, 4}))),
                new int[]{4, 4, 4});
        System.out.println("All tests passed.");
    }
}
