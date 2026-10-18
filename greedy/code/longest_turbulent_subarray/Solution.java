import java.util.*;

public class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int n = arr.length;
        if (n == 1) return 1;
        int[] inc = new int[n]; // turbulent length ending here with arr[i-1] < arr[i]
        int[] dec = new int[n]; // turbulent length ending here with arr[i-1] > arr[i]
        Arrays.fill(inc, 1);
        Arrays.fill(dec, 1);
        int best = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i - 1]) inc[i] = dec[i - 1] + 1;
            else if (arr[i] < arr[i - 1]) dec[i] = inc[i - 1] + 1;
            best = Math.max(best, Math.max(inc[i], dec[i]));
        }
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxTurbulenceSize(new int[]{9, 4, 2, 10, 7, 8, 8, 1, 9}) == 5;
        assert sol.maxTurbulenceSize(new int[]{4, 8, 12, 16}) == 2;
        assert sol.maxTurbulenceSize(new int[]{100}) == 1;
        assert sol.maxTurbulenceSize(new int[]{9, 9}) == 1;
        System.out.println("All tests passed.");
    }
}
