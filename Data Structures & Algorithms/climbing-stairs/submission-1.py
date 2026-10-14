class Solution:
    def climbStairs(self, n: int) -> int:
        memo: list[int | None] = [None] * (n + 1)

        def distinct_branches(idx: int) -> int:
            if idx > n:
                return 0
            if idx == n:
                return 1

            if memo[idx] is not None:
                return memo[idx]

            memo[idx] = distinct_branches(idx + 1) + distinct_branches(idx + 2)
            return memo[idx]

        return distinct_branches(0)