import java.util.*;

public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (ListNode h : lists) if (h != null) pq.offer(h);
        ListNode dummy = new ListNode(0), cur = dummy;
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            cur.next = node; cur = cur.next;
            if (node.next != null) pq.offer(node.next);
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
        ListNode[] lists = {build(1,4,5), build(1,3,4), build(2,6)};
        assert Arrays.equals(toArr(sol.mergeKLists(lists)), new int[]{1,1,2,3,4,4,5,6});
        assert sol.mergeKLists(new ListNode[]{}) == null;
        assert sol.mergeKLists(new ListNode[]{null}) == null;
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
