from collections import deque


class Solution:
    """
    ## 649. Dota2 Senate

    In the Dota2 world, the senate consists of senators from two parties: Radiant (R) and Dire (D).
    Each senator can either ban another senator's right or announce victory if all remaining senators
    are from their party. Both sides act optimally. Return the winning party.

    ### Example
    ```text
    Input:  senate = "RD"
    Output: "Radiant"

    Input:  senate = "RDD"
    Output: "Dire"
    ```

    ### Constraints
    - 1 <= senate.length <= 10^4
    - senate[i] is either 'R' or 'D'
    """

    def predictPartyVictory(self, senate: str) -> str:
        # Two queues of indices; smaller index bans the other party's next senator
        # Re-enqueue the winner with index += n to maintain relative order
        # O(n) time, O(n) space — queue simulation
        radiant = deque()
        dire = deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            # Whoever has the lower index acts first and bans the other
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"


if __name__ == '__main__':
    s = Solution()
    assert s.predictPartyVictory("RD") == "Radiant"
    assert s.predictPartyVictory("RDD") == "Dire"
    assert s.predictPartyVictory("R") == "Radiant"
    assert s.predictPartyVictory("DDRRR") == "Dire"
    print("All tests passed.")
