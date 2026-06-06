from typing import List
import heapq


class Solution:
    """
    ## 1851. Minimum Interval to Include Each Query

    You are given a 2D integer array intervals and an integer array queries.
    For each query, find the size (end - start + 1) of the smallest interval containing
    the query point. Return -1 if no such interval exists.

    ### Example
    ```text
    Input:  intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
    Output: [3,3,1,4]
    (query 2: [2,4] size 3; query 3: [2,4] size 3; query 4: [4,4] size 1; query 5: [3,6] size 4)

    Input:  intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
    Output: [2,-1,4,6]
    ```

    ### Constraints
    - 1 <= intervals.length <= 10^5
    - 1 <= queries.length <= 10^5
    - 1 <= intervals[i][0] <= intervals[i][1] <= 10^7
    - 1 <= queries[i] <= 10^7
    """

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by length; sort queries with original indices
        # Sweep queries in order; add intervals that start <= query to a min-heap by size
        # Pop intervals from heap that end < query; top of heap is the answer
        # O((n + q) log n) time, O(n + q) space — sort intervals and queries, sweep with min heap
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        result = [-1] * len(queries)
        heap = []  # (size, end) — min heap by interval size
        i = 0

        for idx, q in sorted_queries:
            # Push all intervals whose start <= q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1
            # Remove intervals that have ended before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[idx] = heap[0][0]

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]
    assert s.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]
    print("All tests passed.")
