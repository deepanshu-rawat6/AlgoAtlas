from typing import List
import math


class Solution:
    """
    ## 2709. Greatest Common Divisor Traversal

    You are given a **0-indexed** integer array `nums`. There is an edge between two indices `i`
    and `j` if and only if `gcd(nums[i], nums[j]) > 1`.

    Return `true` if all the indices can be traversed (i.e., the graph is connected), or `false`
    otherwise.

    Note that a graph is connected if there is a path between every pair of vertices.

    ---

    ### Examples

    ```text
    Input:  nums = [2,3,6]
    Output: true
    Explanation: 2 and 6 share factor 2; 3 and 6 share factor 3. All connected.

    Input:  nums = [3,9,5]
    Output: false
    Explanation: 5 shares no factor with 3 or 9.

    Input:  nums = [4,3,12,8]
    Output: true
    ```

    ---

    ### Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^5`
    """

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # Union-Find: connect indices that share a common prime factor
        # Factorize each number; union it with any previous number sharing a prime
        # All indices reachable iff they all belong to the same component
        # O(n * sqrt(max_val)) — Union-Find connecting indices via shared prime factors
        if len(nums) == 1:
            return True

        parent = list(range(len(nums) + 100001))  # indices 0..n-1, primes mapped to n+prime
        rank = [0] * (len(nums) + 100001)
        n = len(nums)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        prime_to_idx = {}  # first index that had this prime factor

        for i, num in enumerate(nums):
            val = num
            d = 2
            while d * d <= val:
                if val % d == 0:
                    if d in prime_to_idx:
                        union(i, prime_to_idx[d])
                    else:
                        prime_to_idx[d] = i
                    while val % d == 0:
                        val //= d
                d += 1
            if val > 1:
                if val in prime_to_idx:
                    union(i, prime_to_idx[val])
                else:
                    prime_to_idx[val] = i

        root = find(0)
        return all(find(i) == root for i in range(n))


if __name__ == '__main__':
    s = Solution()
    assert s.canTraverseAllPairs([2, 3, 6]) == True
    assert s.canTraverseAllPairs([3, 9, 5]) == False
    assert s.canTraverseAllPairs([4, 3, 12, 8]) == True
    assert s.canTraverseAllPairs([1]) == True
    assert s.canTraverseAllPairs([2, 2]) == True

    print("All tests passed.")
