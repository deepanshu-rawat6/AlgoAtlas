import heapq
from collections import Counter, deque
from typing import List


class Solution:
    """
    ## 621. Task Scheduler

    Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter
    represents a different task. Tasks could be done in any order. Each task is done in one unit of
    time. For each unit of time, the CPU could complete either one task or just be idle.

    However, there is a non-negative integer `n` that represents the cooldown interval between two
    **same tasks** (the same letter in the array), that is that there must be at least `n` units of
    time between any two same tasks.

    Return the **least number of units of times** that the CPU will take to finish all the given tasks.

    ### Examples

    ```text
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8

    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
    ```

    ```text
    Input: tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6
    ```

    ```text
    Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    Output: 16
    ```

    ### Constraints
    - `1 <= tasks.length <= 10^4`
    - `tasks[i]` is an uppercase English letter.
    - `0 <= n <= 100`
    """

    def leastInterval_heap(self, tasks: List[str], n: int) -> int:
        # O(t * n) — simulate with max-heap and cooldown queue
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)
        time = 0
        cooldown: deque = deque()  # (available_time, neg_count)
        while heap or cooldown:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1  # decrement count
                if cnt < 0:
                    cooldown.append((time + n, cnt))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])
        return time

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Most frequent task determines idle time needed
        # Formula: (max_freq - 1) * (n + 1) + count_of_max_freq_tasks
        # But if tasks fill all slots, answer is just len(tasks)
        # O(t) — math formula based on most frequent task
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + num_max)


if __name__ == '__main__':
    s = Solution()
    assert s.leastInterval_heap(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8

    assert s.leastInterval_heap(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6

    assert s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16

    print("All tests passed.")
