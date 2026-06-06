from typing import List


class Solution:
    """
    ## 978. Longest Turbulent Subarray

    A subarray is turbulent if the comparison sign alternates between each adjacent pair.
    Return the length of the longest turbulent subarray.

    ### Example
    ```text
    Input:  arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    Output: 5  (subarray [4, 2, 10, 7, 8])

    Input:  arr = [4, 8, 12, 16]
    Output: 2

    Input:  arr = [100]
    Output: 1
    ```

    ### Constraints
    - 1 <= arr.length <= 4 * 10^4
    - 0 <= arr[i] <= 10^9
    """

    def maxTurbulenceSize_window(self, arr: List[int]) -> int:
        # O(n) time, O(1) space — sliding window, reset on equal or non-alternating
        n = len(arr)
        if n == 1:
            return 1
        best = cur = 1
        for i in range(1, n):
            cmp = (arr[i] > arr[i-1]) - (arr[i] < arr[i-1])  # -1, 0, or 1
            if cmp == 0:
                cur = 1
            elif i == 1 or cmp == ((arr[i-1] > arr[i-2]) - (arr[i-1] < arr[i-2])):
                cur = 2
            else:
                cur += 1
            best = max(best, cur)
        return best

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Sliding window: extend if alternating comparison sign, else reset to 2 or 1
        # Track current turbulent length and update global max
        # O(n) time, O(n) space — DP with inc/dec arrays
        n = len(arr)
        if n == 1:
            return 1
        inc = [1] * n  # length of turbulent subarray ending here with arr[i-1] < arr[i]
        dec = [1] * n  # length of turbulent subarray ending here with arr[i-1] > arr[i]
        best = 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                inc[i] = dec[i-1] + 1
            elif arr[i] < arr[i-1]:
                dec[i] = inc[i-1] + 1
            best = max(best, inc[i], dec[i])
        return best


if __name__ == '__main__':
    s = Solution()
    assert s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
    assert s.maxTurbulenceSize([4, 8, 12, 16]) == 2
    assert s.maxTurbulenceSize([100]) == 1
    assert s.maxTurbulenceSize([9, 9]) == 1
    assert s.maxTurbulenceSize_window([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
    assert s.maxTurbulenceSize_window([4, 8, 12, 16]) == 2
    assert s.maxTurbulenceSize_window([100]) == 1
    print("All tests passed.")
