import java.util.*;

// LC 706: Design HashMap — chaining approach O(1) avg time, O(n) space
class MyHashMap {
    private static final int SIZE = 1000;
    private List<int[]>[] buckets;

    @SuppressWarnings("unchecked")
    MyHashMap() {
        buckets = new List[SIZE];
        for (int i = 0; i < SIZE; i++) buckets[i] = new ArrayList<>();
    }

    private int hash(int key) { return key % SIZE; }

    public void put(int key, int value) {
        List<int[]> bucket = buckets[hash(key)];
        for (int[] pair : bucket) {
            if (pair[0] == key) { pair[1] = value; return; }
        }
        bucket.add(new int[]{key, value});
    }

    public int get(int key) {
        for (int[] pair : buckets[hash(key)])
            if (pair[0] == key) return pair[1];
        return -1;
    }

    public void remove(int key) {
        List<int[]> bucket = buckets[hash(key)];
        bucket.removeIf(pair -> pair[0] == key);
    }
}

public class Solution {
    public static void main(String[] args) {
        MyHashMap hm = new MyHashMap();
        hm.put(1, 1);
        hm.put(2, 2);
        assert hm.get(1) == 1 : "test 1";
        assert hm.get(3) == -1 : "test 2";
        hm.put(2, 1);
        assert hm.get(2) == 1 : "test 3";
        hm.remove(2);
        assert hm.get(2) == -1 : "test 4";
        System.out.println("All tests passed.");
    }
}
