import java.util.*;

class TimeMap {
    private Map<String, List<int[]>> timestamps;
    private Map<String, List<String>> values;

    public TimeMap() {
        timestamps = new HashMap<>();
        values = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        timestamps.computeIfAbsent(key, k -> new ArrayList<>()).add(new int[]{timestamp});
        values.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
    }

    public String get(String key, int timestamp) {
        List<int[]> ts = timestamps.get(key);
        if (ts == null || ts.isEmpty()) return "";
        int lo = 0, hi = ts.size() - 1, res = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (ts.get(mid)[0] <= timestamp) {
                res = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return res >= 0 ? values.get(key).get(res) : "";
    }
}

public class Solution {
    public static void main(String[] args) {
        TimeMap tm = new TimeMap();
        tm.set("foo", "bar", 1);
        assert tm.get("foo", 1).equals("bar") : "test 1 failed";
        assert tm.get("foo", 3).equals("bar") : "test 2 failed";
        tm.set("foo", "bar2", 4);
        assert tm.get("foo", 4).equals("bar2") : "test 3 failed";
        assert tm.get("foo", 5).equals("bar2") : "test 4 failed";
        assert tm.get("foo", 0).equals("") : "test 5 failed";
        System.out.println("All tests passed.");
    }
}
