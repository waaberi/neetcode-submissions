from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @cache
        def rec(idx: int) -> int:
            if idx >= len(cost):
                return 0
            return cost[idx] + min(rec(idx + 1), rec(idx + 2))

        return min(rec(0), rec(1))
