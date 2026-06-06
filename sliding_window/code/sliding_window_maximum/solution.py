from typing import List
from collections import deque


class Solution:
    """
    ## 239. Sliding Window Maximum

    You are given an array of integers `nums`, there is a sliding window of size `k`
    which is moving from the very left of the array to the very right. You can only see
    the `k` numbers in the window. Each time the sliding window moves right by one
    position.

    Return the max sliding window — an array of the maximum values in each window
    position.

    ### Examples

    ```text
    Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]

    Input:  nums = [1], k = 1
    Output: [1]
    ```

    ### Constraints

    - `1 <= nums.length <= 10^5`
    - `-10^4 <= nums[i] <= 10^4`
    - `1 <= k <= nums.length`
    """

    def maxSlidingWindow_brute(self, nums: List[int], k: int) -> List[int]:
        # For each window position, compute max with built-in — O(n*k)
        # O(n * k) time, O(1) extra space
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic deque: front always holds index of current window's max
        # Pop from back any index whose value <= current (they can never be max)
        # Pop from front if that index has slid out of the current window
        # O(n) time, O(k) space
        dq: deque[int] = deque()  # stores indices, decreasing by value
        result: List[int] = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if dq[0] < i - k + 1:
                dq.popleft()
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert sol.maxSlidingWindow_brute([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow_brute([1], 1) == [1]
    print("All tests passed.")
