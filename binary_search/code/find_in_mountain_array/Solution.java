import java.util.*;

class MountainArray {
    private int[] arr;
    private int calls;

    MountainArray(int[] arr) {
        this.arr = arr;
        this.calls = 0;
    }

    public int get(int index) {
        assert ++calls <= 100 : "Exceeded 100 API calls";
        return arr[index];
    }

    public int length() {
        return arr.length;
    }
}

public class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();

        // 1. Find peak
        int lo = 0, hi = n - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        int peak = lo;

        // 2. Binary search ascending left half
        lo = 0; hi = peak;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = mountainArr.get(mid);
            if (val == target) return mid;
            else if (val < target) lo = mid + 1;
            else hi = mid - 1;
        }

        // 3. Binary search descending right half
        lo = peak + 1; hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = mountainArr.get(mid);
            if (val == target) return mid;
            else if (val > target) lo = mid + 1;
            else hi = mid - 1;
        }

        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findInMountainArray(3, new MountainArray(new int[]{1,2,3,4,5,3,1})) == 2 : "test 1 failed";
        assert sol.findInMountainArray(3, new MountainArray(new int[]{0,1,2,4,2,1})) == -1 : "test 2 failed";
        assert sol.findInMountainArray(1, new MountainArray(new int[]{1,2,3,4,5,3,1})) == 0 : "test 3 failed";
        assert sol.findInMountainArray(5, new MountainArray(new int[]{1,2,3,4,5,3,1})) == 4 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
