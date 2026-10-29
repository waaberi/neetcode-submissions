class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp: list[list[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # def rec(i: int, j: int) -> int:
        #     if i >= m:
        #         return 0
        #     if j >= n:
        #         return 0

        #     take = (1 + rec(i + 1, j + 1)) if text1[i] == text2[j] else 0
        #     skip = max(rec(i + 1, j), rec(i, j + 1))
            
        #     return max(take, skip)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                take = (1 + dp[i + 1][j + 1]) if text1[i] == text2[j] else 0
                skip = max(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(take, skip)
        

        return dp[0][0]