from typing import List


class Solution:
    """
    ## LC 26: Remove Duplicates from Sorted Array

    Given an integer array `nums` sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once. The
    relative order of the elements should be kept the same. Return the number
    of unique elements `k`.

    The first `k` elements of `nums` should hold the unique values. The remaining
    elements do not matter.

    ### Examples

    ```text
    Input:  nums = [1,1,2]
    Output: 2, nums = [1,2,_]

    Input:  nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    ```

    ### Constraints

    - `1 <= nums.length <= 3 * 10^4`
    - `-100 <= nums[i] <= 100`
    - `nums` is sorted in non-decreasing order.
    """

    def method_set(self, nums: List[int]) -> int:
        """O(n) time, O(n) space."""
        # Collect unique elements via set, sort them, overwrite nums in-place
        unique = sorted(set(nums))
        for i, v in enumerate(unique):
            nums[i] = v
        return len(unique)

    def removeDuplicates(self, nums: List[int]) -> int:
        """O(n) time, O(1) space."""
        # k is the write pointer for unique elements
        # Since array is sorted, a new unique element is found when nums[i] != nums[i-1]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2], f"Failed: k={k}, nums={nums}"

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4], f"Failed: k={k}, nums={nums}"

    nums = [1]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1], f"Failed: k={k}, nums={nums}"

    print("All tests passed.")
