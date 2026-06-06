from typing import List


class Solution:
    """
    ## 860. Lemonade Change

    At a lemonade stand, each lemonade costs $5. Customers pay with $5, $10, or $20 bills.
    You start with no change. Return true if you can provide every customer with correct change.

    ### Example
    ```text
    Input:  bills = [5, 5, 5, 10, 20]
    Output: true

    Input:  bills = [5, 5, 10, 10, 20]
    Output: false
    ```

    ### Constraints
    - 1 <= bills.length <= 10^5
    - bills[i] is either 5, 10, or 20
    """

    def lemonadeChange(self, bills: List[int]) -> bool:
        # Track $5 and $10 bills; greedily use $10 before $5 when making $15 change
        # O(n) time, O(1) space
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.lemonadeChange([5, 5, 5, 10, 20]) == True
    assert s.lemonadeChange([5, 5, 10, 10, 20]) == False
    assert s.lemonadeChange([5]) == True
    assert s.lemonadeChange([10]) == False
    print("All tests passed.")
