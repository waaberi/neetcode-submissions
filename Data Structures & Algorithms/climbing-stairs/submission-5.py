class Solution:
    def climbStairs(self, n: int) -> int:
        memo: list[int] = [0] * (n + 2)
        memo[n] = 1

        for idx in range(n-1, -1, -1):
            memo[idx] = memo[idx + 1] + memo[idx + 2]

        return memo[0]