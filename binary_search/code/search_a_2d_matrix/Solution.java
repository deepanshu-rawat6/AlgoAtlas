import java.util.*;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int lo = 0, hi = m * n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            else if (val < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] mat = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        assert sol.searchMatrix(mat, 3) : "test 1 failed";
        assert !sol.searchMatrix(mat, 13) : "test 2 failed";
        assert sol.searchMatrix(mat, 1) : "test 3 failed";
        assert !sol.searchMatrix(mat, 100) : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
