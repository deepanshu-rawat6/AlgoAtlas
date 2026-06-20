from typing import List


class Solution:
    """
    **LC 779: K-th Symbol in Grammar**

    We build a table of `n` rows (1-indexed). We start by writing `0` in the 1st row.
    In every subsequent row, we look at the previous row and replace each occurrence of:
    * `0` with `01`
    * `1` with `10`

    Given two integers `n` and `k`, return the `k`-th (1-indexed) symbol in the `n`-th row.

    ```text
    Row 1: 0
    Row 2: 01
    Row 3: 0110
    Row 4: 01101001
    ```

    Example 1:
    ```text
    Input:  n = 1, k = 1
    Output: 0
    ```

    Example 2:
    ```text
    Input:  n = 2, k = 1
    Output: 0
    ```

    Example 3:
    ```text
    Input:  n = 2, k = 2
    Output: 1
    ```

    **Constraints:**
    * `1 <= n <= 30`
    * `1 <= k <= 2^(n - 1)`
    """

    def kthGrammar(self, n: int, k: int) -> int:
        # Each row is double the previous; k-th symbol in row n mirrors row n-1
        # If k <= mid: same as parent symbol; if k > mid: flip the parent symbol (XOR 1)
        # your code here
        def solve(n, k):
            if n == 1 and k == 1:
                return 0
            mid = 2 ** (n - 2)

            if k <= mid:
                return solve(n - 1, k)
            else:
                return solve(n - 1, k - mid) ^ 1
        
        return solve(n, k)
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: expected 0
    print(sol.kthGrammar(1, 1))

    # Example 2: expected 0
    print(sol.kthGrammar(2, 1))

    # Example 3: expected 1
    print(sol.kthGrammar(2, 2))
