import java.util.*;

public class Solution {
    public int josephusSimulation(int n, int k) {
        List<Integer> people = new ArrayList<>();
        for (int i = 0; i < n; i++) people.add(i);
        int idx = 0;
        while (people.size() > 1) {
            idx = (idx + k - 1) % people.size();
            people.remove(idx);
            if (idx == people.size()) idx = 0;
        }
        return people.get(0);
    }

    public int josephus(int n, int k) {
        if (n == 1) return 0;
        return (josephus(n - 1, k) + k) % n;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.josephus(7, 3) == 3 : "test failed";
        assert sol.josephusSimulation(7, 3) == 3 : "test failed";
        assert sol.josephus(1, 1) == 0 : "test failed";
        assert sol.josephus(5, 2) == 2 : "test failed";
        assert sol.josephusSimulation(5, 2) == 2 : "test failed";
        System.out.println("All tests passed.");
    }
}
