"""
# LC 282: Expression Add Operators

Given a string of digits and a target value, add binary operators (+, -, *)
between the digits to make the expression evaluate to the target.
Return all valid expressions.

## Examples

```text
Input:  num = "123", target = 6
Output: ["1+2+3", "1*2*3"]

Input:  num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Input:  num = "3456237490", target = 9191
Output: []
```

## Constraints
- 1 <= num.length <= 10
- num consists of only digits
- -2^31 <= target <= 2^31 - 1
"""
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Backtracking: at each position, choose how many digits to take as operand
        # Track: current expression string, running total, previous operand (for * precedence)
        # Key insight for multiplication: undo previous addition, apply multiply
        #   e.g., "2+3*4" = (2+3) then *4 → need to undo +3: (5-3) + (3*4) = 14
        result = []

        def backtrack(idx, expr, total, prev):
            # Base case: used all digits
            if idx == len(num):
                if total == target:
                    result.append(expr)
                return

            # Try all possible operands starting at idx
            for i in range(idx, len(num)):
                # No leading zeros (except "0" itself)
                if i > idx and num[idx] == '0':
                    break

                curr_str = num[idx:i + 1]
                curr_val = int(curr_str)

                if idx == 0:
                    # First number: no operator before it
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    # Try +
                    backtrack(i + 1, expr + '+' + curr_str,
                              total + curr_val, curr_val)
                    # Try -
                    backtrack(i + 1, expr + '-' + curr_str,
                              total - curr_val, -curr_val)
                    # Try * (undo prev, apply prev*curr)
                    backtrack(i + 1, expr + '*' + curr_str,
                              total - prev + prev * curr_val, prev * curr_val)

        backtrack(0, "", 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.addOperators("123", 6))    # ["1+2+3", "1*2*3"]
    print(sol.addOperators("232", 8))    # ["2*3+2", "2+3*2"]
    print(sol.addOperators("105", 5))    # ["1*0+5", "10-5"]
