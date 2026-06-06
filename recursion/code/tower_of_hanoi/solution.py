from typing import List


class Solution:
    def towerOfHanoi(self, n: int, src: str, dest: str, aux: str) -> List[str]:
        # Recursive approach: T(n) = 2*T(n-1) + 1 = 2^n - 1 total moves
        # Step 1: move n-1 disks from src to aux (using dest as helper)
        # Step 2: move the nth (largest) disk from src to dest
        # Step 3: move n-1 disks from aux to dest (using src as helper)
        moves = []

        def hanoi(n, src, dest, aux):
            if n == 1:
                moves.append(f"{src}->{dest}")
                return
            hanoi(n - 1, src, aux, dest)   # move n-1 disks out of the way
            moves.append(f"{src}->{dest}")  # move largest disk
            hanoi(n - 1, aux, dest, src)   # move n-1 disks to destination

        hanoi(n, src, dest, aux)
        return moves


if __name__ == "__main__":
    sol = Solution()
    # n=2: A->B, A->C, B->C
    assert sol.towerOfHanoi(2, "A", "C", "B") == ["A->B", "A->C", "B->C"]
    # n=1: single move
    assert sol.towerOfHanoi(1, "A", "C", "B") == ["A->C"]
    # n=3: 7 moves
    result = sol.towerOfHanoi(3, "A", "C", "B")
    assert len(result) == 7  # 2^3 - 1
    print("All tests passed.")
