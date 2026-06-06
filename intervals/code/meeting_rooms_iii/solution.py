from typing import List
import heapq


class Solution:
    """
    ## 2402. Meeting Rooms III

    You have n rooms numbered 0 to n-1. Meetings are given as [start, end] (half-open).
    Each meeting is assigned to the lowest-numbered available room. If no room is free,
    the meeting is delayed until the earliest room becomes free (duration preserved).
    Return the room that held the most meetings (lowest index on tie).

    ### Example
    ```text
    Input:  n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
    Output: 0

    Input:  n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    Output: 1
    ```

    ### Constraints
    - 1 <= n <= 100
    - 1 <= meetings.length <= 10^5
    - 0 <= start_i < end_i <= 5 * 10^5
    """

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Two heaps: available rooms (min-heap of room indices) and busy rooms (end_time, room)
        # Free up rooms whose end_time <= current meeting start before assigning
        # If no room available, wait for earliest-ending room; track usage count per room
        # O(m log n) time, O(n) space — two heaps: available rooms and ongoing meetings
        meetings.sort()
        available = list(range(n))          # min-heap of free room indices
        ongoing = []                         # min-heap of (end_time, room_index)
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that have finished
            while ongoing and ongoing[0][0] <= start:
                _, room = heapq.heappop(ongoing)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(ongoing, (end, room))
            else:
                # Delay: use the room that finishes earliest
                finish, room = heapq.heappop(ongoing)
                heapq.heappush(ongoing, (finish + (end - start), room))

            count[room] += 1

        return count.index(max(count))


if __name__ == '__main__':
    s = Solution()
    assert s.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
    assert s.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
    assert s.mostBooked(1, [[0, 1], [1, 2], [2, 3]]) == 0
    print("All tests passed.")
