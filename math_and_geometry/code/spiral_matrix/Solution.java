import java.util.*;

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        // Shrink boundaries after each side — O(m*n) time
        List<Integer> result = new ArrayList<>();
        int top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1;
        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; c++) result.add(matrix[top][c]);
            for (int r = top + 1; r <= bottom; r++) result.add(matrix[r][right]);
            if (top < bottom) for (int c = right - 1; c >= left; c--) result.add(matrix[bottom][c]);
            if (left < right) for (int r = bottom - 1; r > top; r--) result.add(matrix[r][left]);
            top++; bottom--; left++; right--;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.spiralOrder(new int[][]{{1,2,3},{4,5,6},{7,8,9}})
                .equals(Arrays.asList(1,2,3,6,9,8,7,4,5));
        assert sol.spiralOrder(new int[][]{{1,2,3,4},{5,6,7,8},{9,10,11,12}})
                .equals(Arrays.asList(1,2,3,4,8,12,11,10,9,5,6,7));
        assert sol.spiralOrder(new int[][]{{1}}).equals(Arrays.asList(1));
        assert sol.spiralOrder(new int[][]{{1,2},{3,4}}).equals(Arrays.asList(1,2,4,3));
        System.out.println("All tests passed.");
    }
}
