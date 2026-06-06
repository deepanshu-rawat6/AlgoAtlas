# Accounts Merge (LC 721)

Given a list of accounts (name + emails), merge accounts that share at least one email.
Return merged accounts with emails sorted, name first.

## Approaches

### 1. DFS on Email Graph
**Complexity:** O(n·k·log(n·k)) time, O(n·k) space (n = accounts, k = emails per account)

Build a map from email → list of account indices. DFS from each unvisited account,
collecting all reachable emails via shared addresses.

**Why it works:** Two accounts are connected if they share an email. DFS traverses the
implicit graph of account connections through shared emails.

### 2. Union-Find on Emails (optimal)
**Complexity:** O(n·k·α(n·k)) time, O(n·k) space

Treat each email as a node. For each account, union all its emails together (using the
first email as the representative). Group emails by their root; attach the account name.

**Why it works:** Union-Find efficiently merges email sets. All emails in the same
component belong to the same person. Grouping by root gives the merged account.

## Key Insight

The problem is **connected component merging** where emails are nodes and accounts
define edges between their emails. Union-Find is the natural fit: union all emails
within an account, then group by component root.

## Edge Cases

- Account with a single email — no merging needed, output as-is.
- Same name but different emails with no overlap — separate accounts.
- Chain merging: account A shares email with B, B shares email with C — all three merge.
- Duplicate emails within the same account — handled naturally by Union-Find.
