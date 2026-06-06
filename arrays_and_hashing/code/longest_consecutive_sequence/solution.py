"""
# LC 128: Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the longest
consecutive elements sequence. You must write an algorithm that runs in O(n) time.

## Examples

```text
Input:  nums = [100,4,200,1,3,2]
Output: 4
Explanation: [1,2,3,4]

Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

## Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive_sort(self, nums: List[int]) -> int:
        """Sorting — O(n log n) time, O(1) extra space."""
        # After deduplication and sorting, consecutive elements differ by 1
        if not nums:
            return 0
        nums = sorted(set(nums))
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best

    def longestConsecutive(self, nums: List[int]) -> int:
        """Hash set — O(n) time, O(n) space."""
        # Only start counting from the beginning of a sequence (n-1 not in set)
        # This ensures each sequence is counted exactly once — O(n) total
        num_set = set(nums)
        best = 0
        for n in num_set:
            if n - 1 not in num_set:
                cur = 1
                while n + cur in num_set:
                    cur += 1
                best = max(best, cur)
        return best


if __name__ == "__main__":
    s = Solution()

    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    assert s.longestConsecutive([1]) == 1

    print("All tests passed.")
