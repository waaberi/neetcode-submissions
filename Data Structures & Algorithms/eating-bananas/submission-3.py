class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_k_valid(k: int) -> bool:
            total_hours = 0

            for banana_count in piles:
                total_hours += (banana_count + k - 1) // k

                if total_hours > h:
                    return False

            return True

        lower = (sum(piles) + h - 1) // h
        upper = max(piles)

        while lower <= upper:
            new_k = (lower + upper) // 2

            if is_k_valid(new_k):
                upper = new_k - 1
            else:
                lower = new_k + 1

        return lower