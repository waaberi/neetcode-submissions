class Solution:
    def climbStairs(self, n: int) -> int:
        memo: list[int | None] = [None] * (n + 2)

        for idx in range(n+1, -1, -1):
            if idx == n + 1:
                memo[idx] = 0
            elif idx == n:
                memo[idx] = 1
            else:
                memo[idx] = memo[idx + 1] + memo[idx + 2]

        return memo[0]