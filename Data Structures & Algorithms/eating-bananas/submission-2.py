from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_k_valid(k: int) -> bool:
            total_hours = 0
            for banana_count in piles:
                total_hours += ceil(banana_count / k)
            return total_hours <= h

        lower = ceil(sum(piles) / h)
        upper = max(piles)
        record = float('inf')

        while lower <= upper:
            new_k = (lower + upper) // 2
            if is_k_valid(new_k):
                upper = new_k - 1
            else:
                lower = new_k + 1

        return lower
        