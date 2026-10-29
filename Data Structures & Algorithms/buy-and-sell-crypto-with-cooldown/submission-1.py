from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: list[list[list[int]]] = [[[0 for _ in range(2)] for _ in range(len(prices) + 1)] for _ in range(len(prices) + 1)]

        for i in range(len(prices), -1, -1):
            last_sell_day = i - 1
            for current_idx in range(len(prices) - 1, -1, -1):
                for is_held in range(2):
                    nothing_ever_happens_opt = dp[i][current_idx + 1][is_held]

                    if last_sell_day > -1 and not is_held and current_idx - 1 == last_sell_day:
                        dp[i][current_idx][is_held] = nothing_ever_happens_opt
                        continue

                    other_option = 0

                    if is_held:
                        # figure out if you can sell
                        other_option = prices[current_idx] + dp[current_idx + 1][current_idx + 1][False]
                    else:
                        # figure out if you can buy
                        other_option = -prices[current_idx] + dp[i][current_idx + 1][True]

                    dp[i][current_idx][is_held] = max(nothing_ever_happens_opt, other_option)

        return dp[0][0][False]