from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        ## 77. Combinations

        Given two integers n and k, return all possible combinations of k numbers
        chosen from the range [1, n]. You may return the answer in any order.

        ### Examples

        ```text
        Input:  n = 4, k = 2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

        Input:  n = 1, k = 1
        Output: [[1]]
        ```

        ### Constraints
        - `1 <= n <= 20`
        - `1 <= k <= n`
        """
        # Choose k numbers from [1..n]; start from 'start' to avoid duplicates
        # Prune: if remaining numbers < k - len(path), can't complete — stop early
        # O(C(n,k) * k) time, O(k) stack space
        result = []

        def bt(start, current):
            if len(current) == k:
                result.append(current[:])
                return
            # prune: need at least (k - len(current)) more numbers
            for i in range(start, n - (k - len(current)) + 2):
                current.append(i)
                bt(i + 1, current)
                current.pop()

        bt(1, [])
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.combine(4, 2)) == sorted([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    assert s.combine(1, 1) == [[1]]
    print("All tests passed.")
