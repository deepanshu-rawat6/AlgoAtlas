# LC 1899 — Merge Triplets to Form Target Triplet

Given triplets and a target, you can merge any two triplets by taking the element-wise max. Return `true` if you can obtain the target triplet.

## Approaches

### 1. Greedy Filter + Accumulate Max
- **Time:** O(n) | **Space:** O(1)
- Skip any triplet where any element exceeds the corresponding target element (merging it would overshoot). For remaining valid triplets, accumulate the element-wise max. Check if the result equals the target.

## Key Insight

A triplet is "safe" to merge only if none of its elements exceed the target. Merging an unsafe triplet would permanently increase some component beyond the target, making it impossible to achieve. Among safe triplets, we want to maximize each component independently — the element-wise max of all safe triplets tells us the best achievable triplet. If it equals the target, we can form it.

## Edge Cases

- No valid triplets (all exceed target in some component): Return `False`.
- Target triplet itself is in the list: Return `True` immediately (it's a valid triplet).
- `target = [3, 2, 5]` but no triplet has all three components ≤ target: Return `False`.
- Multiple triplets needed to cover all three target components: The accumulation handles this.
