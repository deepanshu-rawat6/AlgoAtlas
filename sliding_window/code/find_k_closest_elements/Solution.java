import java.util.*;

public class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int lo = 0, hi = arr.length - k;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (x - arr[mid] > arr[mid + k] - x) lo = mid + 1;
            else hi = mid;
        }
        List<Integer> res = new ArrayList<>();
        for (int i = lo; i < lo + k; i++) res.add(arr[i]);
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findClosestElements(new int[]{1,2,3,4,5}, 4, 3).equals(List.of(1,2,3,4));
        assert sol.findClosestElements(new int[]{1,2,3,4,5}, 4, -1).equals(List.of(1,2,3,4));
        assert sol.findClosestElements(new int[]{1,2,3,4,5}, 4, 10).equals(List.of(2,3,4,5));
        System.out.println("All tests passed.");
    }
}
