# Boats to Save People (LC 881)

Given an array `people` of weights and a boat `limit`, each boat carries at most 2 people
with total weight ≤ limit. Return the minimum number of boats needed.

## Approaches

### 1. Brute Force — O(n²) time, O(n) space
Repeatedly find the heaviest person and try to pair them with the lightest that fits.

**Why it works:** Greedy pairing is correct, but without sorting it requires O(n) scans per person.

### 2. Sort + Two Pointers — O(n log n) time, O(1) space
Sort the array. Use left (lightest) and right (heaviest) pointers. Always send the heaviest person; pair with the lightest if they fit together. Each iteration uses exactly one boat.

**Why it works:** The heaviest person must go on some boat. Pairing them with the lightest possible person is optimal — if the lightest can't pair with the heaviest, they can't pair with anyone heavier, so the heaviest goes alone.

## Key Insight
Always send the heaviest person. Greedily pair them with the lightest if possible. Sorting makes this O(n) after the sort.

## Edge Cases
- Single person → one boat
- All people at exactly `limit` weight → each person gets their own boat
- Two people whose combined weight equals `limit` → share a boat
- All people have the same weight
