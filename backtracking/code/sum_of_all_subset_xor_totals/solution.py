"""
# LC 1863: Sum of All Subset XOR Totals

The XOR total of an array is the bitwise XOR of all its elements, or 0 if the array is
empty. Given an array `nums`, return the sum of all XOR totals for every subset of
`nums`. Subsets with the same elements at different indices are counted separately.

## Examples
```text
Input:  nums = [1, 3]
Output: 6
Explanation: subsets [], [1], [3], [1,3] have XOR totals 0, 1, 3, 2 -> sum = 6

Input:  nums = [5, 1, 6]
Output: 28
```

## Constraints
- 1 <= nums.length <= 12
- 1 <= nums[i] <= 20
"""
from typing import List


class Solution:
    def subsetXORSum_brute(self, nums: List[int]) -> int:
        """
        ## 1863. Sum of All Subset XOR Totals

        The XOR total of an array is defined as the XOR of all its elements, or 0 if the
        array is empty. Given an array nums, return the sum of all XOR totals for every
        subset of nums.

        ### Examples

        ```text
        Input:  nums = [1, 3]
        Output: 6
        Explanation: subsets -> [], [1], [3], [1,3]
                     XOR    ->  0,   1,   3,    2   => sum = 6

        Input:  nums = [5, 1, 6]
        Output: 28

        Input:  nums = [3, 4, 5, 6, 7, 8]
        Output: 480
        ```

        ### Constraints
        - `1 <= nums.length <= 12`
        - `1 <= nums[i] <= 20`
        """
        # O(2^n * n) time, O(n) space
        n = len(nums)
        total = 0
        for mask in range(1 << n):
            xor = 0
            for i in range(n):
                if mask & (1 << i):
                    xor ^= nums[i]
            total += xor
        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        """Bit manipulation: OR all elements, multiply by 2^(n-1)."""
        # For each element, branch: include in XOR or skip
        # Sum XOR values of all subsets at leaf nodes
        # O(n) time, O(1) space
        or_all = 0
        for x in nums:
            or_all |= x
        return or_all * (1 << (len(nums) - 1))


if __name__ == '__main__':
    s = Solution()
    assert s.subsetXORSum([1, 3]) == 6
    assert s.subsetXORSum([5, 1, 6]) == 28
    assert s.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480
    assert s.subsetXORSum_brute([1, 3]) == 6
    assert s.subsetXORSum_brute([5, 1, 6]) == 28
    print("All tests passed.")
