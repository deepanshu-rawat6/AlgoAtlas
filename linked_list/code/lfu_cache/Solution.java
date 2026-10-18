import java.util.*;

public class Solution {
    static class LFUCache {
        private final int cap;
        private int minFreq;
        private final Map<Integer, Integer> keyVal = new HashMap<>();
        private final Map<Integer, Integer> keyFreq = new HashMap<>();
        private final Map<Integer, LinkedHashSet<Integer>> freqKeys = new HashMap<>();

        LFUCache(int capacity) { cap = capacity; }

        private void update(int key) {
            int freq = keyFreq.get(key);
            freqKeys.get(freq).remove(key);
            if (freqKeys.get(freq).isEmpty() && freq == minFreq) minFreq++;
            keyFreq.put(key, freq + 1);
            freqKeys.computeIfAbsent(freq + 1, k -> new LinkedHashSet<>()).add(key);
        }

        int get(int key) {
            if (!keyVal.containsKey(key)) return -1;
            update(key);
            return keyVal.get(key);
        }

        void put(int key, int value) {
            if (cap == 0) return;
            if (keyVal.containsKey(key)) {
                keyVal.put(key, value);
                update(key);
            } else {
                if (keyVal.size() >= cap) {
                    int evict = freqKeys.get(minFreq).iterator().next();
                    freqKeys.get(minFreq).remove(evict);
                    keyVal.remove(evict);
                    keyFreq.remove(evict);
                }
                keyVal.put(key, value);
                keyFreq.put(key, 1);
                freqKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
                minFreq = 1;
            }
        }
    }

    public static void main(String[] args) {
        LFUCache c = new LFUCache(2);
        c.put(1, 1);
        c.put(2, 2);
        assert c.get(1) == 1;
        c.put(3, 3);
        assert c.get(2) == -1;
        assert c.get(3) == 3;
        c.put(4, 4);
        assert c.get(1) == -1;
        assert c.get(3) == 3;
        assert c.get(4) == 4;

        LFUCache c2 = new LFUCache(0);
        c2.put(0, 0);
        assert c2.get(0) == -1;

        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
