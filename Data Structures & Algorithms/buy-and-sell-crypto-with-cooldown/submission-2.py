from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp: list[list[list[int]]] = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for has_coin in range(2):
                for cooldown in range(2):
                    nothing_option = dp[i + 1][has_coin][False]
                    other_option = 0

                    if has_coin:
                        other_option = prices[i] + dp[i + 1][False][True]
                    elif not cooldown:
                        other_option = -prices[i] + dp[i + 1][True][False]

                    dp[i][has_coin][cooldown] = max(nothing_option, other_option)
        
        return dp[0][False][False]