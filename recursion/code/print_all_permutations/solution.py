"""
# Print All Permutations

Given an array of distinct integers `nums`, return all possible permutations.

## Examples
```text
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Constraints
- Elements are distinct; the result contains n! permutations.
"""
from typing import List


class Solution:
    def permute_swap(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Swap-based O(n!)
        # Fix one element at position `start` by swapping it with each element,
        # then recurse on the remaining suffix.
        result = []

        def recurse(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # fix nums[i] at start
                recurse(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack

        recurse(0)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach 2: Pick from remaining O(n!)
        # At each step, pick any unused element for the current position.
        result = []

        def recurse(current, remaining):
            if not remaining:
                result.append(current)
                return
            for i in range(len(remaining)):
                recurse(current + [remaining[i]], remaining[:i] + remaining[i+1:])

        recurse([], nums)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sol.permute_swap([1, 2, 3])
    r2 = sol.permute([1, 2, 3])
    assert len(r1) == 6
    assert len(r2) == 6
    assert sorted(r1) == sorted(r2)
    # Single element
    assert sol.permute([1]) == [[1]]
    print("All tests passed.")
