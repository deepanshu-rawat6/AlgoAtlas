# LC 136 — Single Number

Every element in the array appears twice except for one. Find that single element. Must use O(n) time and O(1) space.

## Approaches

### 1. Hash Set
- **Time:** O(n) | **Space:** O(n)
- Add unseen numbers to a set; remove them when seen again. The remaining element is the single number.

### 2. XOR
- **Time:** O(n) | **Space:** O(1)
- XOR all numbers together. Pairs cancel out (`a ^ a = 0`), and `0 ^ x = x`, leaving only the single number.

## Key Insight

XOR is commutative and associative, and `a ^ a = 0` for any `a`. XORing all elements together means every duplicate pair cancels to 0, and the single element XORed with 0 gives itself. This is the canonical O(1) space solution — no sorting, no hashing, just a single pass with one variable.

## Edge Cases

- Single element array: Return that element.
- All pairs except one: XOR handles any arrangement.
- Negative numbers: XOR works on the bit representation, handles negatives correctly.
- The single number can be 0: `0 ^ 0 = 0` for pairs, and the single 0 remains.
