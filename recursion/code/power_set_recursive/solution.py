"""
# Power Set (Recursive)

Given an array `nums`, return all possible subsets (the power set). The
solution set must not contain duplicate subsets.

## Examples
```text
Input:  nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
```

## Constraints
- Uses the include/exclude decision pattern at each index.
- Produces 2^n subsets; input is assumed to contain distinct elements.
"""
from typing import List


class Solution:
    def powerSet(self, nums: List[int]) -> List[List[int]]:
        # Include/exclude pattern: at each index, branch into two choices.
        # Total subsets = 2^n (each element is either in or out).
        result = []

        def recurse(idx, current):
            if idx == len(nums):
                result.append(current[:])  # base case: all elements decided
                return
            # Exclude nums[idx]
            recurse(idx + 1, current)
            # Include nums[idx]
            current.append(nums[idx])
            recurse(idx + 1, current)
            current.pop()  # backtrack

        recurse(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    result = sol.powerSet([1, 2, 3])
    assert len(result) == 8  # 2^3 subsets
    # Check empty set and full set are present
    assert [] in result
    assert [1, 2, 3] in result
    # Single element
    assert len(sol.powerSet([1])) == 2
    # Empty input
    assert sol.powerSet([]) == [[]]
    print("All tests passed.")
