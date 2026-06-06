# Product of Array Except Self (LC 238)

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product
of all elements except `nums[i]`. Must run in O(n) without using division.

## Approaches

### 1. Brute Force — O(n²) time, O(1) extra space
For each index, multiply all other elements. Simple but too slow.

**Why it works:** Correct by definition, but redundantly recomputes products.

### 2. Prefix + Suffix Arrays — O(n) time, O(n) extra space
`prefix[i]` = product of all elements left of `i`. `suffix[i]` = product of all elements right of `i`. Answer is `prefix[i] * suffix[i]`.

**Why it works:** Every element's "except self" product is exactly the product of everything to its left times everything to its right.

### 3. Single Output Array — O(n) time, O(1) extra space
First pass: fill `answer[i]` with running left-product up to `i-1`. Second pass: multiply in running right-product from `i+1` onward.

**Why it works:** Reuses the output array to store the left-product, then multiplies in the right-product in a second pass — no extra arrays needed.

## Key Insight
`answer[i] = (product of all left of i) × (product of all right of i)`. Two passes over the output array compute both without division.

## Edge Cases
- Array contains zeros — products of other elements may be zero
- Single zero in array — all positions except the zero position become 0
- Two or more zeros — all positions become 0
- Negative numbers (handled naturally by multiplication)
