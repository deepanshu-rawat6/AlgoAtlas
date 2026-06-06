from typing import List
import heapq


class Solution:
    """
    ## 253. Meeting Rooms II

    Given an array of meeting time intervals, return the minimum number of conference rooms required.

    ### Example
    ```text
    Input:  intervals = [[0,30],[5,10],[15,20]]
    Output: 2

    Input:  intervals = [[7,10],[2,4]]
    Output: 1
    ```

    ### Constraints
    - 1 <= intervals.length <= 10^4
    - 0 <= start_i < end_i <= 10^6
    """

    def minMeetingRooms_heap(self, intervals: List[List[int]]) -> int:
        # O(n log n) time, O(n) space — sort + min heap of end times
        intervals.sort(key=lambda x: x[0])
        heap = []  # min-heap of end times
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Min-heap of end times: if next meeting starts after earliest end, reuse room
        # Otherwise allocate a new room; heap size = rooms needed
        # O(n log n) time, O(n) space — chronological ordering with start/end events
        starts = sorted(s for s, _ in intervals)
        ends = sorted(e for _, e in intervals)
        rooms = end_ptr = 0
        for start in starts:
            if start < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1
        return rooms


if __name__ == '__main__':
    s = Solution()
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms([[1, 5], [2, 6], [3, 7]]) == 3
    assert s.minMeetingRooms_heap([[0, 30], [5, 10], [15, 20]]) == 2
    print("All tests passed.")
