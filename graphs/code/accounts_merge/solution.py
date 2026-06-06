from typing import List
from collections import defaultdict


class Solution:
    """
    ## 721. Accounts Merge

    Given a list of `accounts` where each element `accounts[i]` is a list of strings,
    where `accounts[i][0]` is a name and the rest are emails belonging to that account.

    Merge accounts that share at least one common email. Return the merged accounts in
    any order. Within each account, return emails in sorted order, with the name first.

    ### Examples

    ```text
    Input:
      accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
      ]
    Output:
      [
        ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
      ]

    Input:
      accounts = [["John","j1@","j2@"],["John","j1@","j3@"]]
    Output:
      [["John","j1@","j2@","j3@"]]
    ```

    ### Constraints

    - `1 <= accounts.length <= 1000`
    - `2 <= accounts[i].length <= 10`
    - `1 <= accounts[i][j].length <= 30`
    - `accounts[i][0]` consists of English letters.
    - `accounts[i][j]` (for `j > 0`) is a valid email.
    """

    def accountsMerge_dfs(self, accounts: List[List[str]]) -> List[List[str]]:
        # O(n*k*log(n*k)) time, O(n*k) space
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_accounts[email].append(i)

        visited_accounts = set()
        result = []

        def dfs(idx: int, emails: set) -> None:
            if idx in visited_accounts:
                return
            visited_accounts.add(idx)
            for email in accounts[idx][1:]:
                emails.add(email)
                for neighbor in email_to_accounts[email]:
                    dfs(neighbor, emails)

        for i in range(len(accounts)):
            if i not in visited_accounts:
                emails: set = set()
                dfs(i, emails)
                result.append([accounts[i][0]] + sorted(emails))
        return result

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union-Find: union all emails within the same account
        # Group emails by their root representative; attach account name
        # O(n*k*alpha(n*k)) time, O(n*k) space — Union-Find
        parent: dict = {}
        rank: dict = {}

        def find(x: str) -> str:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: str, y: str) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            if rank.get(px, 0) < rank.get(py, 0):
                px, py = py, px
            parent[py] = px
            if rank.get(px, 0) == rank.get(py, 0):
                rank[px] = rank.get(px, 0) + 1

        email_to_name: dict = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)

        groups: dict = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]


if __name__ == '__main__':
    s = Solution()

    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    res = s.accountsMerge(accounts1)
    assert len(res) == 3

    accounts2 = [["John", "j1@", "j2@"], ["John", "j1@", "j3@"]]
    res2 = s.accountsMerge(accounts2)
    assert len(res2) == 1 and sorted(res2[0][1:]) == ["j1@", "j2@", "j3@"]

    res3 = s.accountsMerge_dfs(accounts2)
    assert len(res3) == 1 and sorted(res3[0][1:]) == ["j1@", "j2@", "j3@"]
    print("All tests passed.")
