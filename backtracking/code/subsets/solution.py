"""
# LC 78: Subsets

Given an integer array `nums` of unique elements, return all possible subsets (the power
set). The solution set must not contain duplicate subsets and may be returned in any
order.

## Examples
```text
Input:  nums = [1, 2, 3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input:  nums = [0]
Output: [[],[0]]
```

## Constraints
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        ## 78. Subsets

        Given an integer array nums of unique elements, return all possible subsets
        (the power set). The solution set must not contain duplicate subsets.
        Return the solution in any order.

        ### Examples

        ```text
        Input:  nums = [1, 2, 3]
        Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

        Input:  nums = [0]
        Output: [[], [0]]
        ```

        ### Constraints
        - `1 <= nums.length <= 10`
        - `-10 <= nums[i] <= 10`
        - All integers in nums are unique.
        """
        # O(2^n) time, O(2^n) space
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Backtracking: build subsets by choosing to include or skip each element."""
        # At each index, branch: include nums[i] or skip it
        # Leaf nodes (i == len(nums)) are complete subsets — add to result
        # O(2^n) time, O(n) stack space
        result = []

        def bt(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                bt(i + 1, current)
                current.pop()

        bt(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    for fn in (s.subsets_iterative, s.subsets):
        assert sorted(fn([1, 2, 3])) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        assert sorted(fn([0])) == sorted([[], [0]])
    print("All tests passed.")
