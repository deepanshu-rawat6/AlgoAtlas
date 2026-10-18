import java.util.*;

public class Solution {
    static class DetectSquares {
        private Map<Long, Integer> ptCount = new HashMap<>();
        private Map<Integer, Set<Integer>> xToYs = new HashMap<>();

        private long key(int x, int y) { return (long) x * 1001 + y; }

        public void add(int[] point) {
            int x = point[0], y = point[1];
            ptCount.merge(key(x, y), 1, Integer::sum);
            xToYs.computeIfAbsent(x, k -> new HashSet<>()).add(y);
        }

        public int count(int[] point) {
            int qx = point[0], qy = point[1];
            int result = 0;
            Set<Integer> ys = xToYs.getOrDefault(qx, Collections.emptySet());
            for (int y : ys) {
                if (y == qy) continue;
                int side = Math.abs(y - qy);
                for (int dx : new int[]{qx + side, qx - side}) {
                    result += ptCount.getOrDefault(key(qx, y), 0)
                            * ptCount.getOrDefault(key(dx, qy), 0)
                            * ptCount.getOrDefault(key(dx, y), 0);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {
        DetectSquares ds = new DetectSquares();
        ds.add(new int[]{3, 10});
        ds.add(new int[]{11, 2});
        ds.add(new int[]{3, 2});
        assert ds.count(new int[]{11, 10}) == 1;
        assert ds.count(new int[]{14, 8}) == 0;
        ds.add(new int[]{11, 2});
        assert ds.count(new int[]{11, 10}) == 2;
        System.out.println("All tests passed.");
    }
}
