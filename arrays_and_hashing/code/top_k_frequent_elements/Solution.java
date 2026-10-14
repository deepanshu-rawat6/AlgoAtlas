import java.util.*;

// LC 347: Top K Frequent Elements
public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Bucket sort by frequency — O(n) time, O(n) space
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) count.merge(n, 1, Integer::sum);

        @SuppressWarnings("unchecked")
        List<Integer>[] buckets = new List[nums.length + 1];
        for (Map.Entry<Integer, Integer> e : count.entrySet()) {
            int freq = e.getValue();
            if (buckets[freq] == null) buckets[freq] = new ArrayList<>();
            buckets[freq].add(e.getKey());
        }

        int[] result = new int[k];
        int idx = 0;
        for (int freq = buckets.length - 1; freq >= 1 && idx < k; freq--) {
            if (buckets[freq] == null) continue;
            for (int num : buckets[freq]) {
                result[idx++] = num;
                if (idx == k) break;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[] r = s.topKFrequent(new int[]{1,1,1,2,2,3}, 2);
        Arrays.sort(r);
        assert Arrays.equals(r, new int[]{1,2}) : "test 1";

        assert Arrays.equals(s.topKFrequent(new int[]{1}, 1), new int[]{1}) : "test 2";

        r = s.topKFrequent(new int[]{1,2}, 2);
        Arrays.sort(r);
        assert Arrays.equals(r, new int[]{1,2}) : "test 3";

        System.out.println("All tests passed.");
    }
}
