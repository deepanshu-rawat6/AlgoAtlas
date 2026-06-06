"""
# 136. Single Number

Given a non-empty array of integers `nums`, every element appears **twice** except for one.
Find that single one.

You must implement a solution with linear runtime complexity and use only constant extra space.

## Examples

```text
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
```

## Constraints
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.
"""

from typing import List


class Solution:
    def singleNumber_set(self, nums: List[int]) -> int:
        # O(n) time, O(n) space — hash set: add if unseen, remove if seen
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return seen.pop()

    def singleNumber(self, nums: List[int]) -> int:
        # XOR all numbers: pairs cancel out (a^a=0), leaving the single number
        # O(n) time, O(1) space — XOR cancels pairs, leaving the single element
        result = 0
        for n in nums:
            result ^= n
        return result


if __name__ == '__main__':
    s = Solution()
    for method in (s.singleNumber_set, s.singleNumber):
        assert method([2, 2, 1]) == 1
        assert method([4, 1, 2, 1, 2]) == 4
        assert method([1]) == 1
    print("All tests passed.")
