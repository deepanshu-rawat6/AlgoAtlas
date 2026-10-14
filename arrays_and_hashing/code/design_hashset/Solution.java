import java.util.*;

// LC 705: Design HashSet — chaining approach O(1) avg time, O(n) space
class MyHashSet {
    private static final int SIZE = 1000;
    private List<Integer>[] buckets;

    @SuppressWarnings("unchecked")
    MyHashSet() {
        buckets = new List[SIZE];
        for (int i = 0; i < SIZE; i++) buckets[i] = new ArrayList<>();
    }

    private int hash(int key) { return key % SIZE; }

    public void add(int key) {
        List<Integer> b = buckets[hash(key)];
        if (!b.contains(key)) b.add(key);
    }

    public void remove(int key) { buckets[hash(key)].remove(Integer.valueOf(key)); }

    public boolean contains(int key) { return buckets[hash(key)].contains(key); }
}

public class Solution {
    public static void main(String[] args) {
        MyHashSet hs = new MyHashSet();
        hs.add(1);
        hs.add(2);
        assert hs.contains(1) : "test 1";
        assert !hs.contains(3) : "test 2";
        hs.add(2);
        assert hs.contains(2) : "test 3";
        hs.remove(2);
        assert !hs.contains(2) : "test 4";
        System.out.println("All tests passed.");
    }
}
