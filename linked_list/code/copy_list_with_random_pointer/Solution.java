import java.util.*;

public class Solution {
    // O(n) space hashmap approach
    public ListNode copyRandomListHashmap(ListNode head) {
        if (head == null) return null;
        Map<ListNode, ListNode> map = new HashMap<>();
        ListNode cur = head;
        while (cur != null) { map.put(cur, new ListNode(cur.val)); cur = cur.next; }
        cur = head;
        while (cur != null) {
            if (cur.next != null) map.get(cur).next = map.get(cur.next);
            if (cur.random != null) map.get(cur).random = map.get(cur.random);
            cur = cur.next;
        }
        return map.get(head);
    }

    // O(1) space interleaving approach
    public ListNode copyRandomList(ListNode head) {
        if (head == null) return null;
        // Step 1: interleave clones (A -> A' -> B -> B' -> ...)
        ListNode cur = head;
        while (cur != null) {
            ListNode clone = new ListNode(cur.val);
            clone.next = cur.next;
            cur.next = clone;
            cur = clone.next;
        }
        // Step 2: assign random pointers
        cur = head;
        while (cur != null) {
            if (cur.random != null) cur.next.random = cur.random.next;
            cur = cur.next.next;
        }
        // Step 3: separate lists
        ListNode dummy = new ListNode(0), cloneCur = dummy;
        cur = head;
        while (cur != null) {
            cloneCur.next = cur.next;
            cur.next = cur.next.next;
            cloneCur = cloneCur.next;
            cur = cur.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // [[7,null],[13,0],[11,4],[10,2],[1,0]]
        int[] vals = {7, 13, 11, 10, 1};
        ListNode[] nodes = new ListNode[5];
        for (int i = 0; i < 5; i++) nodes[i] = new ListNode(vals[i]);
        for (int i = 0; i < 4; i++) nodes[i].next = nodes[i + 1];
        nodes[1].random = nodes[0]; nodes[2].random = nodes[4];
        nodes[3].random = nodes[2]; nodes[4].random = nodes[0];

        ListNode copy1 = sol.copyRandomListHashmap(nodes[0]);
        assert copy1 != nodes[0];
        assert copy1.val == 7;
        assert copy1.next.val == 13;
        assert copy1.next.random.val == 7;

        ListNode[] nodes2 = new ListNode[5];
        for (int i = 0; i < 5; i++) nodes2[i] = new ListNode(vals[i]);
        for (int i = 0; i < 4; i++) nodes2[i].next = nodes2[i + 1];
        nodes2[1].random = nodes2[0]; nodes2[2].random = nodes2[4];
        nodes2[3].random = nodes2[2]; nodes2[4].random = nodes2[0];

        ListNode copy2 = sol.copyRandomList(nodes2[0]);
        assert copy2 != nodes2[0];
        assert copy2.val == 7;
        assert copy2.next.random.val == 7;

        assert sol.copyRandomList(null) == null;
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
