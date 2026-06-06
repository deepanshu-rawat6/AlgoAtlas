# Daily Temperatures (LC 739)

Given daily temperatures, return an array where each entry is the number of days until a warmer temperature. If no warmer day exists, use 0.

## Approaches

### 1. Brute Force
- **Time:** O(n²) | **Space:** O(1) extra
- For each day, scan forward until a warmer day is found.

### 2. Monotonic Decreasing Stack
- **Time:** O(n) | **Space:** O(n)
- Maintain a stack of **indices** of days with unresolved warmer days.
- When a warmer temperature arrives at index `i`, pop all indices from the stack whose temperature is less than `temperatures[i]` and set `answer[idx] = i - idx`.
- The stack stays in decreasing order of temperatures (monotonic decreasing).

## Key Insight

The stack holds indices of days "waiting" for a warmer day. When a warmer day arrives, it resolves all waiting days that are cooler — in one sweep. Each index is pushed once and popped once → O(n) total. Days that never get resolved stay on the stack and keep their default value of 0.

## Edge Cases

- Strictly decreasing temperatures → stack fills up, nothing is ever popped → all answers are 0.
- Strictly increasing temperatures → each new day resolves all previous days.
- All same temperatures → no day is warmer than another → all answers are 0.
- Single element → answer is `[0]`.
