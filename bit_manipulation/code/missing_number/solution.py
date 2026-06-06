"""
# 268. Missing Number

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`,
return the only number in the range that is missing from the array.

## Examples

```text
Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

## Constraints
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.
"""

from typing import List


class Solution:
    def missingNumber_sum(self, nums: List[int]) -> int:
        # O(n) time, O(1) space — expected sum minus actual sum
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def missingNumber(self, nums: List[int]) -> int:
        # XOR all indices 0..n with all values; pairs cancel, leaving the missing number
        # O(n) time, O(1) space — XOR all indices and values; pairs cancel out
        result = len(nums)
        for i, n in enumerate(nums):
            result ^= i ^ n
        return result


if __name__ == '__main__':
    s = Solution()
    for method in (s.missingNumber_sum, s.missingNumber):
        assert method([3, 0, 1]) == 2
        assert method([0, 1]) == 2
        assert method([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All tests passed.")
