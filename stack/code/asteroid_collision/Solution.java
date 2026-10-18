import java.util.*;

public class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        // Only collisions happen when a left-moving asteroid meets a right-moving one on stack
        // Keep destroying top of stack while it's smaller than the incoming asteroid
        // Equal sizes destroy both; larger stack top destroys incoming
        // O(n) time, O(n) space — stack simulation of collisions
        Deque<Integer> stack = new ArrayDeque<>();
        for (int a : asteroids) {
            boolean alive = true;
            while (alive && a < 0 && !stack.isEmpty() && stack.peek() > 0) {
                if (stack.peek() < -a) {
                    stack.pop();           // right asteroid destroyed
                } else if (stack.peek() == -a) {
                    stack.pop();           // both destroyed
                    alive = false;
                } else {
                    alive = false;         // left asteroid destroyed
                }
            }
            if (alive) stack.push(a);
        }
        int n = stack.size();
        int[] result = new int[n];
        // stack.pop() returns top (most recently pushed); fill from end to restore order
        for (int i = n - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(sol.asteroidCollision(new int[]{5, 10, -5}), new int[]{5, 10}) : "test 1 failed";
        assert Arrays.equals(sol.asteroidCollision(new int[]{8, -8}), new int[]{}) : "test 2 failed";
        assert Arrays.equals(sol.asteroidCollision(new int[]{10, 2, -5}), new int[]{10}) : "test 3 failed";
        assert Arrays.equals(sol.asteroidCollision(new int[]{-2, -1, 1, 2}), new int[]{-2, -1, 1, 2}) : "test 4 failed";
        assert Arrays.equals(sol.asteroidCollision(new int[]{1, -1}), new int[]{}) : "test 5 failed";
        System.out.println("All tests passed.");
    }
}
