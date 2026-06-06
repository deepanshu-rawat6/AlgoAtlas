from typing import List


class Solution:
    """
    ## 918. Maximum Sum Circular Subarray

    Given a circular integer array nums, return the maximum possible sum of a non-empty subarray.
    A circular array means the end of the array connects to the beginning.

    ### Example
    ```text
    Input:  nums = [1, -2, 3, -2]
    Output: 3  (subarray [3])

    Input:  nums = [5, -3, 5]
    Output: 10  (subarray [5, 5] wrapping around)

    Input:  nums = [-3, -2, -3]
    Output: -2
    ```

    ### Constraints
    - 1 <= nums.length <= 3 * 10^4
    - -3 * 10^4 <= nums[i] <= 3 * 10^4
    """

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Case 1: max subarray is non-wrapping — standard Kadane's
        # Case 2: max subarray wraps — equals total_sum - min_subarray_sum
        # Edge case: if all elements negative, return max (min subarray = whole array)
        # O(n) time, O(1) space — Kadane's for both max and min subarray
        total = sum(nums)
        max_sum = cur_max = nums[0]
        min_sum = cur_min = nums[0]
        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        # If all negative, max_sum is the answer (total - min_sum would be 0)
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([-3, -2, -3]) == -2
    print("All tests passed.")
