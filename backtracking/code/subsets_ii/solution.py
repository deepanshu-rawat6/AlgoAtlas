"""
# LC 90: Subsets II

Given an integer array `nums` that may contain duplicates, return all possible subsets
(the power set). The solution set must not contain duplicate subsets and may be returned
in any order.

## Examples
```text
Input:  nums = [1, 2, 2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input:  nums = [0]
Output: [[],[0]]
```

## Constraints
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        ## 90. Subsets II

        Given an integer array nums that may contain duplicates, return all possible
        subsets (the power set). The solution set must not contain duplicate subsets.
        Return the solution in any order.

        ### Examples

        ```text
        Input:  nums = [1, 2, 2]
        Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]

        Input:  nums = [0]
        Output: [[], [0]]
        ```

        ### Constraints
        - `1 <= nums.length <= 10`
        - `-10 <= nums[i] <= 10`
        """
        # Sort first so duplicates are adjacent and easy to skip
        # Skip duplicate values at the same recursion level to avoid duplicate subsets
        # O(2^n) time, O(n) stack space
        nums.sort()
        result = []

        def bt(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                bt(i + 1, current)
                current.pop()

        bt(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.subsetsWithDup([1, 2, 2])) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    assert sorted(s.subsetsWithDup([0])) == sorted([[], [0]])
    print("All tests passed.")
