"""
# 682. Baseball Game

## Problem
You are keeping score for a baseball game with special rules. Given a list of
operations, calculate the sum of all valid scores.

Operations:
- Integer string: record a new score of that value
- `"+"`: record a new score that is the sum of the previous two scores
- `"D"`: record a new score that is double the previous score
- `"C"`: invalidate the previous score, removing it from the record

## Examples
```text
Input:  operations = ["5","2","C","D","+"]
Output: 30
Explanation:
  "5" -> record [5]
  "2" -> record [5, 2]
  "C" -> remove last -> [5]
  "D" -> double last -> [5, 10]
  "+" -> sum last two -> [5, 10, 15]
  Total = 5 + 10 + 15 = 30

Input:  operations = ["5","-2","4","C","D","9","+","+"]
Output: 27
```

## Constraints
- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer
  in the range `[-3 * 10^4, 3 * 10^4]`
- For `"+"`, there will always be at least two previous scores
- For `"C"` and `"D"`, there will always be at least one previous score
"""

from typing import List


class Solution:
    def calPoints_list(self, operations: List[str]) -> int:
        # Simulate the record: C removes last, D doubles last, + sums last two
        # O(n) time, O(n) space — list as mutable record
        record = []
        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
        return sum(record)

    def calPoints(self, operations: List[str]) -> int:
        # Same logic with explicit stack name for clarity
        # O(n) time, O(n) space — explicit stack (same logic, named for clarity)
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert s.calPoints(["1"]) == 1
    print("All tests passed.")
