import java.util.*;

// Design problem: Solution IS the FreqStack.
// freq map tracks how many times each value has been pushed.
// group map maps each frequency level to a stack of values pushed at that frequency.
// maxFreq tracks the current maximum frequency.
// O(1) push and pop — each element is touched at most twice per frequency level.
public class Solution {
    private Map<Integer, Integer> freq = new HashMap<>();             // val -> frequency
    private Map<Integer, Deque<Integer>> group = new HashMap<>();    // freq -> stack of vals
    private int maxFreq = 0;

    public void push(int val) {
        // Increment frequency of val; append to the group for that frequency
        // Update maxFreq if this val's frequency is now the highest
        // O(1)
        freq.merge(val, 1, Integer::sum);
        int f = freq.get(val);
        maxFreq = Math.max(maxFreq, f);
        group.computeIfAbsent(f, k -> new ArrayDeque<>()).push(val);
    }

    public int pop() {
        // Pop from the group at maxFreq (most recently pushed among most frequent)
        // Decrement val's frequency; if maxFreq group is now empty, decrease maxFreq
        // O(1)
        int val = group.get(maxFreq).pop();
        freq.merge(val, -1, Integer::sum);
        if (group.get(maxFreq).isEmpty()) maxFreq--;
        return val;
    }

    public static void main(String[] args) {
        Solution fs = new Solution();
        for (int v : new int[]{5, 7, 5, 7, 4, 5}) fs.push(v);
        assert fs.pop() == 5 : "pop 1 failed";  // freq {5:3, 7:2, 4:1} -> 5
        assert fs.pop() == 7 : "pop 2 failed";  // freq {5:2, 7:2, 4:1} -> 7 (most recent at freq 2)
        assert fs.pop() == 5 : "pop 3 failed";  // freq {5:2, 7:1, 4:1} -> 5
        assert fs.pop() == 4 : "pop 4 failed";  // freq {5:1, 7:1, 4:1} -> 4 (most recent at freq 1)
        System.out.println("All tests passed.");
    }
}
