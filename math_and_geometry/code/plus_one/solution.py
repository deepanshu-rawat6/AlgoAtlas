"""
# 66. Plus One

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]`
is the i-th digit of the integer. The digits are ordered from most significant to least significant.

Increment the large integer by one and return the resulting array of digits.

## Examples

```text
Input: digits = [1,2,3]
Output: [1,2,4]

Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Input: digits = [9]
Output: [1,0]
```

## Constraints
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Add 1 from the last digit; propagate carry leftward
        # If carry remains after all digits, prepend 1
        # O(n) time, O(1) extra space — iterate from end propagating carry
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == '__main__':
    s = Solution()
    assert s.plusOne([1,2,3]) == [1,2,4]
    assert s.plusOne([9]) == [1,0]
    assert s.plusOne([9,9]) == [1,0,0]
    assert s.plusOne([4,3,2,1]) == [4,3,2,2]
    print("All tests passed.")
