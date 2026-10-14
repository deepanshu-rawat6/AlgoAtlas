import java.util.*;

// LC 229: Majority Element II
public class Solution {
    public List<Integer> majorityElementHashmap(int[] nums) {
        // Count all; return those > n/3 — O(n) time, O(n) space
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) count.merge(n, 1, Integer::sum);
        int threshold = nums.length / 3;
        List<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : count.entrySet())
            if (e.getValue() > threshold) result.add(e.getKey());
        return result;
    }

    public List<Integer> majorityElement(int[] nums) {
        // Boyer-Moore extended (at most 2 candidates) — O(n) time, O(1) space
        int cand1 = 0, cand2 = 1, cnt1 = 0, cnt2 = 0;
        for (int n : nums) {
            if (n == cand1)      cnt1++;
            else if (n == cand2) cnt2++;
            else if (cnt1 == 0)  { cand1 = n; cnt1 = 1; }
            else if (cnt2 == 0)  { cand2 = n; cnt2 = 1; }
            else                 { cnt1--; cnt2--; }
        }
        int threshold = nums.length / 3;
        List<Integer> result = new ArrayList<>();
        int c1 = 0, c2 = 0;
        for (int n : nums) {
            if (n == cand1) c1++;
            else if (n == cand2) c2++;
        }
        if (c1 > threshold) result.add(cand1);
        if (c2 > threshold) result.add(cand2);
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<Integer> r;

        r = s.majorityElement(new int[]{3,2,3});
        Collections.sort(r);
        assert r.equals(List.of(3)) : "test 1";

        r = s.majorityElement(new int[]{1});
        assert r.equals(List.of(1)) : "test 2";

        r = s.majorityElement(new int[]{1,2});
        Collections.sort(r);
        assert r.equals(List.of(1,2)) : "test 3";

        r = s.majorityElement(new int[]{1,1,1,3,3,2,2,2});
        Collections.sort(r);
        assert r.equals(List.of(1,2)) : "test 4";

        System.out.println("All tests passed.");
    }
}
