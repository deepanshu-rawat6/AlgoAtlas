from typing import List


class Solution:
    """
    **LC 1863: Sum of All Subset XOR Totals**

    The **XOR total** of an array is defined as the bitwise XOR of all its elements,
    or `0` if the array is empty.
    * e.g. the XOR total of `[2, 5, 6]` is `2 XOR 5 XOR 6 = 1`

    Given an array `nums`, return the **sum of all XOR totals** for every subset of `nums`.

    Note: subsets with the same elements but derived independently are counted separately.

    Example 1:
    ```text
    Input:  nums = [1, 3]
    Output: 6
    Explanation: subsets → [], [1], [3], [1,3]
                 XOR totals → 0, 1, 3, 2  →  sum = 6
    ```

    Example 2:
    ```text
    Input:  nums = [5, 1, 6]
    Output: 28
    Explanation: subsets → [], [5], [1], [6], [5,1], [5,6], [1,6], [5,1,6]
                 XOR totals → 0, 5, 1, 6, 4, 3, 7, 2  →  sum = 28
    ```

    Example 3:
    ```text
    Input:  nums = [3, 4, 5, 6, 7, 8]
    Output: 480
    ```

    **Constraints:**
    * `1 <= nums.length <= 12`
    * `1 <= nums[i] <= 20`
    """

    def subsetXORSum(self, nums: List[int]) -> int:
        # Approach: backtracking over all subsets
        # 1. At each index, branch: include nums[i] in current XOR or skip it
        # 2. At leaf (index == len(nums)), add current XOR value to total sum
        # 3. Math shortcut: answer = OR of all nums, shifted left by (n-1)
        # your code here
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: expected 6
    print(sol.subsetXORSum([1, 3]))

    # Example 2: expected 28
    print(sol.subsetXORSum([5, 1, 6]))

    # Example 3: expected 480
    print(sol.subsetXORSum([3, 4, 5, 6, 7, 8]))
