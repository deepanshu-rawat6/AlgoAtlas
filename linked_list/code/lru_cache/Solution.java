import java.util.*;

public class Solution {
    // LinkedHashMap with access-order=true; removeEldestEntry auto-evicts LRU
    static class LRUCache extends LinkedHashMap<Integer, Integer> {
        private final int cap;

        LRUCache(int capacity) { super(capacity, 0.75f, true); cap = capacity; }

        int get(int key) {
            // super.get triggers afterNodeAccess (moves to MRU end)
            Integer v = super.get(key);
            return v == null ? -1 : v;
        }

        void put(int key, int value) { super.put(key, value); }

        @Override
        protected boolean removeEldestEntry(Map.Entry<Integer, Integer> e) {
            return size() > cap;
        }
    }

    public static void main(String[] args) {
        LRUCache c = new LRUCache(2);
        c.put(1, 1);
        c.put(2, 2);
        assert c.get(1) == 1;
        c.put(3, 3);
        assert c.get(2) == -1;
        c.put(4, 4);
        assert c.get(1) == -1;
        assert c.get(3) == 3;
        assert c.get(4) == 4;
        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
