"""
# LC 1: Two Sum

Given an array of integers `nums` and an integer `target`, return *indices* of the
two numbers such that they add up to `target`. You may assume exactly one solution
exists, and you may not use the same element twice.

## Examples

```text
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]

Input:  nums = [3,2,4], target = 6
Output: [1,2]

Input:  nums = [3,3], target = 6
Output: [0,1]
```

## Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""
from typing import List


class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        # Try every pair (i, j) — O(n^2) because we check all combinations
        # O(n^2) time | O(1) space
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a hash map to remember each number's index as we scan
        # For each number, compute what complement is needed to reach target
        # If complement already seen, we found our pair in O(1) lookup
        # O(n) time | O(n) space
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("All tests passed.")
