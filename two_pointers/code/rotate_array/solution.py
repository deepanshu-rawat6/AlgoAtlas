from typing import List


class Solution:
    """
    ## LC 189 — Rotate Array

    Given an integer array `nums`, rotate the array to the right by `k` steps,
    where `k` is non-negative. Modify `nums` in-place.

    ### Examples

    ```text
    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]

    Input:  nums = [-1, -100, 3, 99], k = 2
    Output: [3, 99, -1, -100]
    ```

    ### Constraints

    - 1 <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1
    - 0 <= k <= 10^5
    """

    def method_brute_force(self, nums: List[int], k: int) -> None:
        """O(n*k) time | O(1) space — rotate one step at a time"""
        # Rotate one step at a time by shifting all elements right — O(n*k)
        n = len(nums)
        k %= n
        for _ in range(k):
            last = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last

    def method_extra_array(self, nums: List[int], k: int) -> None:
        """O(n) time | O(n) space"""
        # Slice the last k elements to front, rest follows — O(n) space
        n = len(nums)
        k %= n
        tmp = nums[-k:] + nums[:-k]
        nums[:] = tmp

    def rotate(self, nums: List[int], k: int) -> None:
        """O(n) time | O(1) space — reverse three times"""
        # Reverse entire array, then reverse first k, then reverse rest k..n-1
        # Three reversals achieve a rotation without extra space
        n = len(nums)
        k %= n

        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)
    print(nums)  # [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    sol.rotate(nums, 2)
    print(nums)  # [3, 99, -1, -100]
