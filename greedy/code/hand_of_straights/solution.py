from typing import List
from collections import Counter


class Solution:
    """
    ## 846. Hand of Straights

    Given an integer array hand and an integer groupSize, return true if the cards can be
    rearranged into groups of groupSize consecutive cards.

    ### Example
    ```text
    Input:  hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
    Output: true  (groups: [1,2,3], [2,3,4], [6,7,8])

    Input:  hand = [1, 2, 3, 4, 5], groupSize = 4
    Output: false
    ```

    ### Constraints
    - 1 <= hand.length <= 10^4
    - 0 <= hand[i] <= 10^9
    - 1 <= groupSize <= hand.length
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sort cards; greedily form groups starting from the smallest card
        # Use a counter; for each group start, consume groupSize consecutive values
        # O(n log n) time, O(n) space — sort + greedy with counter
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                need = count[card]
                for i in range(groupSize):
                    if count[card + i] < need:
                        return False
                    count[card + i] -= need
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True
    assert s.isNStraightHand([1, 2, 3, 4, 5], 4) == False
    assert s.isNStraightHand([1, 2, 3], 3) == True
    assert s.isNStraightHand([1], 1) == True
    print("All tests passed.")
