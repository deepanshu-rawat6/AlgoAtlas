"""
# LC 1929: Concatenation of Array

Given an integer array `nums` of length `n`, return an array `ans` of length `2n`
where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for all `0 <= i < n`.

## Examples

```text
Input:  nums = [1,2,1]
Output: [1,2,1,1,2,1]

Input:  nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
```

## Constraints
- n == nums.length
- 1 <= n <= 1000
- 1 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def getConcatenation_brute(self, nums: List[int]) -> List[int]:
        # Append all elements twice using a loop
        # O(n) time | O(n) space
        ans = []
        for _ in range(2):
            for n in nums:
                ans.append(n)
        return ans

    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Python list concatenation creates a new list with both copies
        # O(n) time | O(n) space
        return nums + nums


if __name__ == "__main__":
    s = Solution()
    assert s.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert s.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    print("All tests passed.")
