from typing import List


class Solution:
    """
    ## 219. Contains Duplicate II

    Given an integer array `nums` and an integer `k`, return `true` if there exist two
    distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and
    `abs(i - j) <= k`.

    ### Examples

    ```text
    Input:  nums = [1, 2, 3, 1], k = 3
    Output: true

    Input:  nums = [1, 0, 1, 1], k = 1
    Output: true

    Input:  nums = [1, 2, 3, 1, 2, 3], k = 2
    Output: false
    ```

    ### Constraints

    - `1 <= nums.length <= 10^5`
    - `-10^9 <= nums[i] <= 10^9`
    - `0 <= k <= 10^5`
    """

    def containsNearbyDuplicate_brute(self, nums: List[int], k: int) -> bool:
        # For each element, check the next k elements for a duplicate — O(n*k)
        # O(n * k) time, O(1) space
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Maintain a sliding set of size k; if new element already in set, found duplicate
        # Remove the element that just fell out of the window (nums[i-k])
        # O(n) time, O(k) space
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
    assert sol.containsNearbyDuplicate_brute([1, 2, 3, 1], 3) == True
    assert sol.containsNearbyDuplicate_brute([1, 2, 3, 1, 2, 3], 2) == False
    print("All tests passed.")
